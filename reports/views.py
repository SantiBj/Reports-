from django.shortcuts import render
from datetime import datetime
from .service.share.selectorTransformData import selectorTransformData
from .service.sales.generatedExcel import generatedExcel
from .service.coeditions.excelCoeditions import excelCoeditions
from django.http import HttpResponse
from .service.share.createZip import createZip
from .service.sales.createPdf import createPdf

# Create your views here.


def insertDataForDB(request):
    return render(request, "reports/insertData.html")


# recibe datos y no hace nada mas
def combinaterPaternOfFileToExcel(request):
    if (request.method == "POST"):
        # devuelve la data de cada caso

        dataFormated = selectorTransformData(request.FILES['file'])
        filesCreated = []
        filesCreatedCoeditors = []

        # añadir los reportes de ventas al array
        if dataFormated["type"] == "sales":
            for numSupplier in dataFormated["sales"].keys():
                filesCreated.append(generatedExcel(
                    dataFormated["sales"][numSupplier], numSupplier))
                filesCreated.append(
                    createPdf(dataFormated["sales"][numSupplier], numSupplier, request))

        if dataFormated["type"] == "coeditions":
            # primero los reportes normales
            for coeditorData in dataFormated["coeditions"]["records"].keys():
                filesCreatedCoeditors.append(excelCoeditions(
                    dataFormated["coeditions"]["records"][coeditorData], coeditorData))
            for codCli in dataFormated["coeditions"]["coeditorsCodCli"].keys():
                filesCreatedCoeditors.append(excelCoeditions(
                    dataFormated["coeditions"]["coeditorsCodCli"][codCli], codCli, True
                ))
            # los reportes con codcli

        # conversion de datos a zip
        contentZip = createZip(filesCreatedCoeditors)

        response = HttpResponse(content_type="application/zip")
        response['Content-Disposition'] = f'attachment; filename=rep-{datetime.now().date()}.zip'
        response.write(contentZip)
        return response
