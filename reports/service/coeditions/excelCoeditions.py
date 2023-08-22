import openpyxl
from datetime import datetime
from ..share.printerDataInSheet import printerDataInSheet
from ..share.calculatedTotals import total
from django.http import HttpResponse
from .fromDictToTuple import formatedFromDictToTuple
from .printerTotal import printerTotal
from ..share.calculatedTotals import calculateTotalWithDataNegative,bookNegativeAndCalculationTotals


def excelCoeditions(dataEditions, cutNumber, codCli=False):
    book = openpyxl.load_workbook("coediciones.xlsx")
    sheet = book.worksheets[0]

    startRow = 5
    startCol = 1

    if codCli:
        recordsCodCli = []

        sheet.cell(row=3, column=2, value=f"Periodo: {datetime.now().date()}")
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
                dataCoeditor.append(formatedFromDictToTuple(recordCodCli))
            printerDataInSheet(dataCoeditor, startRow, startCol, sheet)
            startRow = startRow + elements + 1
            

        # total sin negativos
        totalsCodCli  = total(recordsCodCli) 
        printerTotal(sheet,totalsCodCli)

        # total negativos
        totalsNegatives = bookNegativeAndCalculationTotals(recordsCodCli)
        if len(totalsNegatives["books"]) > 0:
            endRow = sheet.max_row+3
            tuplesNegatives = []
            for bookNegative in totalsNegatives['books']:
                tuplesNegatives.append(formatedFromDictToTuple(bookNegative))
            printerDataInSheet(tuplesNegatives,endRow,1,sheet)
            endRow = sheet.max_row+1
            sheet.cell(row=endRow,column=6,value="Total =")
            sheet.cell(row=endRow,column=7,value=totalsNegatives["quantity"])
            sheet.cell(row=endRow,column=8,value=totalsNegatives["grossTotal"])
            sheet.cell(row=endRow,column=10,value=totalsNegatives["netTotal"])

            #total con negativos
            endRow = sheet.max_row+3
            fullTotal = calculateTotalWithDataNegative(totalsCodCli,totalsNegatives)
            sheet.cell(row=endRow,column=6,value="Total =")
            sheet.cell(row=endRow,column=7,value=fullTotal["quantity"])
            sheet.cell(row=endRow,column=8,value=fullTotal["grossTotal"])
            sheet.cell(row=endRow,column=10,value=fullTotal["netTotal"])

        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename=COED-{dataEditions[nCutCodCli][0]["COEDITOR"][:15]}.xlsx'
        book.save(response)
        return response
    
    else:
        dataInTuples = []
        for record in dataEditions:
            dataInTuples.append(formatedFromDictToTuple(record))
        sheet.cell(row=2, column=2, value=dataEditions[0]["COEDITOR"])
        sheet.cell(
            row=3, column=2, value=f"Periodo: {datetime.now().date()}     N° corte: {cutNumber}")
        printerDataInSheet(dataInTuples, startRow, startCol, sheet)

        totalsCoeditor = total(dataEditions)
        # total sin negativos
        printerTotal(sheet,totalsCoeditor)


        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename=COED-{dataEditions[0]["COEDITOR"]}.xlsx'
        book.save(response)
        return response
