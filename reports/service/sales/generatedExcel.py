import openpyxl
from django.http import HttpResponse
from ..share.calculatedTotals import calculatedTotalsBySupplier
from datetime import datetime
from .formatedRecordForDictToTuple import formatedRecordForDictToTuple
from ..share.printerDataInSheet import printerDataInSheet


def generatedExcel(dataDict, cutNumber):
    isUEX = True if "SAP" in dataDict[0] else False
    # si es UEX usar otra plantilla y otro formateador
    dataInTuples = []
    for record in dataDict:
        dataInTuples.append(formatedRecordForDictToTuple(record,isUEX))

    book = openpyxl.load_workbook("plantilla-UEX.xlsx" if isUEX else "plantilla-reporte-ventas.xlsx")
    sheet = book.worksheets[0]

    startRow = 5
    startCol = 1

    # añadiendo cabecera
    sheet.cell(row=2, column=2, value=f"Proveedor: {dataDict[0]['PROVEEDOR']}")
    sheet.cell(row=3, column=2,
               value=f"Periodo: {datetime.now().date()}     N° corte: {cutNumber}")

    #añadiendo registros al excel
    printerDataInSheet(dataInTuples,startRow,startCol,sheet)
    

    # calculo de total cantidad,bruto,neto
    calculatedTotalsBySupplier(dataDict, sheet,isUEX)

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename={dataDict[0]["PROVEEDOR"][:3]}.xlsx'
    book.save(response)
    return response