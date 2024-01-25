from django.shortcuts import render
from datetime import datetime
from .service.share.selectorTransformData import selectorTransformData
from .service.sales.generatedExcel import generatedExcel
from .service.coeditions.excelCoeditions import excelCoeditions
from django.http import HttpResponse
from .service.share.createZip import createZip
from .service.sales.createPdf import createPdf
from .service.coeditions.pdfCoeditors import createPdf as pdfCoeditors

# Create your views here.


def insertDataForDB(request):
    return render(request, "reports/insertData.html")


def combinaterPaternOfFileToExcel(request):
    if (request.method == "POST"):
        # devuelve la data de cada caso
        dataFormated = selectorTransformData(request.FILES['file'])
        filesCreated = []
        filesCreatedCoeditors = []

        # añadir los reportes de ventas al array
        if dataFormated["type"] == "sales":
            for numSupplier in dataFormated["sales"].keys():
                hasSap = False
                for data in dataFormated["sales"][numSupplier]:
                    if "SAP" in data:
                        hasSap = True
                        break

                filesCreated.append(generatedExcel(
                    dataFormated["sales"][numSupplier], numSupplier,hasSap))
                filesCreated.append(
                    createPdf(dataFormated["sales"][numSupplier], numSupplier, request,hasSap))

        if dataFormated["type"] == "coeditions":
            # primero los reportes normales
            for coeditorNum in dataFormated["coeditions"]["records"].keys():
                hasSap = False
                for coeditor in dataFormated["coeditions"]["records"][coeditorNum]:
                    if "SAP" in coeditor:
                        hasSap = True
                        break

                filesCreatedCoeditors.append(excelCoeditions(
                    dataFormated["coeditions"]["records"][coeditorNum], coeditorNum, hasSap=hasSap))
                filesCreatedCoeditors.append(pdfCoeditors(
                    dataFormated["coeditions"]["records"][coeditorNum], coeditorNum, request,hasSap=hasSap
                )
                )
            # reportes codcli
            for codCli in dataFormated["coeditions"]["coeditorsCodCli"].keys():
                hasSap = False
                keysCoeditor = list(dataFormated["coeditions"]["coeditorsCodCli"][codCli].keys(
                ))
                for key in keysCoeditor:
                    for data in dataFormated["coeditions"]["coeditorsCodCli"][codCli][key]:
                        if "SAP" in data:
                            hasSap = True
                            break

                filesCreatedCoeditors.append(excelCoeditions(
                    dataFormated["coeditions"]["coeditorsCodCli"][codCli], codCli, hasSap=hasSap, codCli=True
                ))
                filesCreatedCoeditors.append(pdfCoeditors(
                    dataFormated["coeditions"]["coeditorsCodCli"][codCli], codCli, request,codCli=True,hasSap=hasSap
                ))

        # conversion de datos a zip
        contentZip = createZip(
            filesCreatedCoeditors if dataFormated["type"] == "coeditions" else filesCreated)

        response = HttpResponse(content_type="application/zip")
        response['Content-Disposition'] = f'attachment; filename=rep-{datetime.now().date()}.zip'
        response.write(contentZip)
        return response
