import openpyxl
from datetime import datetime
from ..share.printerDataInSheet import printerDataInSheet
from ..share.calculatedTotals import total
from django.http import HttpResponse
from .fromDictToTuple import formatedFromDictToTuple




def excelCoeditions(dataEditions,cutNumber):
# usar una funcion para pintar los datos diferente en los andes
    dataInTuples = []
    for record in dataEditions:
        dataInTuples.append(formatedFromDictToTuple(record))
    
    book = openpyxl.load_workbook("coediciones.xlsx")
    sheet = book.worksheets[0]

    startRow = 5
    startCol = 1

    sheet.cell(row=2,column=2,value=dataEditions[0]["COEDITOR"])
    sheet.cell(row=3,column=2,value=f"Periodo: {datetime.now().date()}     N° corte: {cutNumber}")

    printerDataInSheet(dataInTuples,startRow,startCol,sheet)
    
    #caculos y pintando data en el excel 
    totalsCoeditor = total(dataEditions)

    endRowInSheet = sheet.max_row+2
    sheet.cell(row=endRowInSheet,column=6,value="Total = ")
    sheet.cell(row=endRowInSheet,column=7,value=totalsCoeditor["totalQuantity"])
    sheet.cell(row=endRowInSheet,column=8,value=totalsCoeditor["totalGrossValue"])
    sheet.cell(row=endRowInSheet,column=10,value=totalsCoeditor["totalNetValue"])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename=COED-{dataEditions[0]["COEDITOR"]}'
    book.save(response)
    return response