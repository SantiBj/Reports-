from django.shortcuts import render,redirect
from datetime import datetime
from .service.transformData import transform
from .service.generatedExcel import generatedExcel
from django.http import HttpResponse
from .service.createZip import createZip
from .service.createPdf import createPdf

# Create your views here.


def insertDataForDB(request):
    return render(request, "reports/insertData.html")

'''
def combinaterPaternOfFileToExcel(request):
    if(request.method == "GET" or 'file' not in request.FILES):
        redirect("/")
    if (request.method == "POST"):
        dataForFiles = transform(request.FILES['file'])
        filesCreated = []
        #add excel for filesCreated
        for numSupplier in dataForFiles.keys():
            filesCreated.append(generatedExcel(dataForFiles[numSupplier],numSupplier))
            filesCreated.append(createPdf(dataForFiles[numSupplier],numSupplier,request))
        
        #conversion de datos a zip
        contentZip = createZip(filesCreated)

        response = HttpResponse(content_type="application/zip")
        response['Content-Disposition'] = f'attachment; filename=rep-{datetime.now().date()}.zip'
        response.write(contentZip)
        return response
'''

#recibe datos y no hace nada mas
def combinaterPaternOfFileToExcel(request):
    if (request.method == "POST"):
        dataForFiles = transform(request.FILES['file'])
        filesCreated = []

        #add excel for filesCreated
        for numSupplier in dataForFiles.keys():
            filesCreated.append(generatedExcel(dataForFiles[numSupplier],numSupplier))
            filesCreated.append(createPdf(dataForFiles[numSupplier],numSupplier,request))
        
        #conversion de datos a zip
        contentZip = createZip(filesCreated)

        response = HttpResponse(content_type="application/zip")
        response['Content-Disposition'] = f'attachment; filename=rep-{datetime.now().date()}.zip'
        response.write(contentZip)
        print(response)
        return response
    else :
        #
        print("hhhs")
        return render(request,"reports/prueba.html")
        

