from django.shortcuts import render
from datetime import datetime
from .service.share.selectorTransformData import selectorTransformData
from .service.sales.generatedExcel import generatedExcel
from django.http import HttpResponse
from .service.share.createZip import createZip
from .service.sales.createPdf import createPdf

# Create your views here.


def insertDataForDB(request):
    return render(request, "reports/insertData.html")


#recibe datos y no hace nada mas
def combinaterPaternOfFileToExcel(request):
    if (request.method == "POST"):
        # devuelve la data de cada caso

        dataFormated = selectorTransformData(request.FILES['file'])
        filesCreated = []

        #añadir los reportes de ventas al array
        for numSupplier in dataFormated["sales"].keys():
            filesCreated.append(generatedExcel(dataFormated["sales"][numSupplier],numSupplier))
            filesCreated.append(createPdf(dataFormated["sales"][numSupplier],numSupplier,request))
        
        #añadir los reportes de ediciones al array
        


        #conversion de datos a zip
        contentZip = createZip(filesCreated)

        response = HttpResponse(content_type="application/zip")
        response['Content-Disposition'] = f'attachment; filename=rep-{datetime.now().date()}.zip'
        response.write(contentZip)
        print(response)
        return response
        

