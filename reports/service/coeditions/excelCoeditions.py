import openpyxl
from datetime import datetime
from ..share.printerDataInSheet import printerDataInSheet
from ..share.calculatedTotals import total
from django.http import HttpResponse
from .fromDictToTuple import formatedFromDictToTuple
from .printerTotal import printerTotal
from ..share.calculatedTotals import calculateTotalWithDataNegative, bookNegativeAndCalculationTotals
from .printers import printerTotalNegatives
from .booksNegToTuple import booksNegToTuple


def defineWorkBook(workBook):
    book = openpyxl.load_workbook(workBook)
    return {
        "book": book,
        "sheet": book.worksheets[0],
    }
def excelCoeditions(dataEditions, cutNumber, hasSap, codCli=False):
    book = None
    sheet = None

    startRow = 5
    startCol = 1

    if codCli:
        recordsCodCli = []
        firstKey = list(dataEditions.keys())[0]

        if hasSap:
            if dataEditions[firstKey][0]["MONEDA"] == "PESOS":
                defineBook = defineWorkBook("coeSapCOP.xlsx")
                book = defineBook["book"]
                sheet = defineBook["sheet"]
            else:
                defineBook =  defineWorkBook("coeSap.xlsx")
                book = defineBook["book"]
                sheet = defineBook["sheet"]
        else:
            if dataEditions[firstKey][0]["MONEDA"] == "PESOS":
                defineBook = defineWorkBook("coedicionesCOP.xlsx")
                book = defineBook["book"]
                sheet = defineBook["sheet"]
            else:
                defineBook = defineWorkBook("coediciones.xlsx")
                book = defineBook["book"]
                sheet = defineBook["sheet"]

        sheet.cell(row=2, column=2, value=f"Elaborado: {dataEditions[firstKey][0]['ELABORADO']}")
        sheet.cell(row=3, column=2,
                   value=f"Periodo: {dataEditions[firstKey][0]['FECHA']}      Moneda:{dataEditions[firstKey][0]['MONEDA']}")
        

        for nCutCodCli in dataEditions.keys():
            # pinta la cabecera
            sheet.cell(row=startRow, column=1,
                       value=f"n° corte {nCutCodCli} dependencia => {dataEditions[nCutCodCli][0]['COEDITOR']}")
            startRow += 1
            dataCoeditor = []
            elements = 0
            for recordCodCli in dataEditions[nCutCodCli]:
                elements += 1
                recordsCodCli.append(recordCodCli)
                dataCoeditor.append(
                    formatedFromDictToTuple(recordCodCli, hasSap))
            printerDataInSheet(dataCoeditor, startRow, startCol, sheet)
            startRow = startRow + elements + 1

        # devoluciones
        totalsNegatives = bookNegativeAndCalculationTotals(recordsCodCli)
        if len(totalsNegatives["books"]) > 0:
            endRow = sheet.max_row+3

            printerDataInSheet(booksNegToTuple(
                totalsNegatives, hasSap), endRow, 1, sheet)
            endRow = sheet.max_row+1

        # total
        endRow = sheet.max_row+3
        totalsCodCli = total(recordsCodCli)
        printerTotal(sheet, totalsCodCli, hasSap)

        dateOfFile = dataEditions[firstKey][0]['FECHA'].split('-')

        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename={dataEditions[nCutCodCli][0]["COEDITOR"][4:30]}{dateOfFile[4]}_{dateOfFile[3]}.xlsx'
        book.save(response)
        return response

    else:
        if hasSap:
            if dataEditions[0]["MONEDA"] == "PESOS":
                defineBook = defineWorkBook("coeSapCOP.xlsx")
                book = defineBook["book"]
                sheet = defineBook["sheet"]
            else:
                defineBook =  defineWorkBook("oeSap.xlsx")
                book = defineBook["book"]
                sheet = defineBook["sheet"]
        else:
            if dataEditions[0]["MONEDA"] == "PESOS":
                defineBook = defineWorkBook("coedicionesCOP.xlsx")
                book = defineBook["book"]
                sheet = defineBook["sheet"]
            else:
                defineBook = defineWorkBook("coediciones.xlsx")
                book = defineBook["book"]
                sheet = defineBook["sheet"]

        dataInTuples = []
        for record in dataEditions:
            dataInTuples.append(formatedFromDictToTuple(record, hasSap))

        sheet.cell(row=2, column=2, value=f"Coeditor: {dataEditions[0]['COEDITOR']}          Elaborado: {dataEditions[0]['ELABORADO']}")
        sheet.cell(
            row=3, column=2, value=f"Periodo: {dataEditions[0]['FECHA']}     N° corte: {cutNumber}     Moneda: {dataEditions[0]['MONEDA']}")
        printerDataInSheet(dataInTuples, startRow, startCol, sheet)

        # libros negativos
        totalsNegatives = bookNegativeAndCalculationTotals(dataEditions)
        if len(totalsNegatives['books']) > 0:
            endRow = sheet.max_row + 2
            # total negativos
            printerDataInSheet(booksNegToTuple(
                totalsNegatives, hasSap), endRow, 1, sheet)
            endRow = endRow = sheet.max_row+1

         # total sin negativos
        totalsCoeditor = total(dataEditions)
        printerTotal(sheet, totalsCoeditor, hasSap)

        dateOfFile = dataEditions[0]['FECHA'].split('-')

        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename={dataEditions[0]["COEDITOR"][4:30]}{dateOfFile[4]}_{dateOfFile[3]}.xlsx'
        book.save(response)
        return response
