from ..sales.formatedRecordForDictToTuple import formatedRecordForDictToTuple
from decimal import Decimal

#suma total bruto, total neto y cantidad de todos los libros del proveedor
def total(recordsSupplier):
        totalQuantity = 0
        totalGrossValue = 0
        totalNetValue = 0

        for record in recordsSupplier:
            totalQuantity += record["CANTIDAD"]
            totalGrossValue += record["VALOR_BRUTO"]
            totalNetValue += record["VALOR_NETO"]
        
        return {
            "totalQuantity":totalQuantity,
            "totalGrossValue":totalGrossValue,
            "totalNetValue":totalNetValue,
        }

def calculatedTotalsBySupplier(recordsSupplier,sheet,isUEX):
    totalV = total(recordsSupplier)
    endRecord = sheet.max_row+2

    if isUEX:
        sheet.cell(row=endRecord,column=8,value="Total =")
        sheet.cell(row=endRecord,column=9,value=totalV["totalQuantity"])
        sheet.cell(row=endRecord,column=10,value=totalV["totalGrossValue"])
        sheet.cell(row=endRecord,column=12,value=totalV["totalNetValue"])
    else:
        sheet.cell(row=endRecord,column=7,value="Total =")
        sheet.cell(row=endRecord,column=8,value=totalV["totalQuantity"])
        sheet.cell(row=endRecord,column=9,value=totalV["totalGrossValue"])
        sheet.cell(row=endRecord,column=11,value=totalV["totalNetValue"])

    #podria indicar el calculo de negativos
    endRecord = sheet.max_row+3
    bookNegative = bookNegativeAndCalculationTotals(recordsSupplier)
    

    #
    if len(bookNegative["books"]) > 0:
        booksWithQuantityNegativeTuple = []

        #añadiendo cada libro con cantidad negativa a una tupla
        for book in bookNegative["books"]:
            booksWithQuantityNegativeTuple.append(formatedRecordForDictToTuple(book,isUEX))

        #pintar los datos y poner los nuevos calculos
        for rowIndex,rowData in enumerate(booksWithQuantityNegativeTuple,start=endRecord):
            for colIndex,value in enumerate(rowData,start=1):
                sheet.cell(row=rowIndex,column=colIndex,value=value)
        
        endRecord = sheet.max_row+1
        # creando cuadro de texto

        #pintando los nuevos totales
        results = calculateTotalWithDataNegative(totalV,bookNegative)
    
        if not isUEX:
            sheet.cell(row=endRecord,column=8,value=results["quantity"])
            sheet.cell(row=endRecord,column=9,value=results["grossTotal"])
            sheet.cell(row=endRecord,column=11,value=results["netTotal"])
        else:
            sheet.cell(row=endRecord,column=9,value=results["quantity"])
            sheet.cell(row=endRecord,column=10,value=results["grossTotal"])
            sheet.cell(row=endRecord,column=12,value=results["netTotal"])

        createChartText(sheet,isUEX)

#realiza el calculo de la suma de libros vendidos
#con libros devueltos
def calculateTotalWithDataNegative(total,totalNegatives):
    return{
        "quantity":total["totalQuantity"]+abs(totalNegatives["quantity"]),
        "grossTotal":total["totalGrossValue"]+abs(totalNegatives["grossTotal"]),
        "netTotal":total["totalNetValue"]+abs(totalNegatives["netTotal"]),
    }

#suma de total bruto, total neto y cantidad de libros devueltos
#retona libros devueltos
def bookNegativeAndCalculationTotals(recordsSupplier):
    booksWithQuantityNegative = []
    totalQuantityNegatives = 0
    totalGrossNegatives = 0
    totalNetNegatives = 0

    for recordT in recordsSupplier:
        if int(recordT["CANTIDAD"]) < 0:
            totalQuantityNegatives += recordT["CANTIDAD"]
            totalGrossNegatives += recordT["VALOR_BRUTO"]
            totalNetNegatives += recordT["VALOR_NETO"]
            booksWithQuantityNegative.append(recordT)
    return {
        "books":booksWithQuantityNegative,
        "quantity":totalQuantityNegatives,
        "grossTotal":totalGrossNegatives,
        "netTotal":totalNetNegatives
    }



def createChartText(sheet,isUEX):
    endRecord = sheet.max_row+3
    text =  '''NOTA: Los valores negativos en la columna CANTIDAD\n
            corresponden a devoluciones en ventas  reportadas\n
            por nuestros clientes durante el periodo en referencia,\n
            por tanto solicitamos a ustedes se sirva expedir\n
            la correspondiente nota crédito y cargar al inventario\n
            de Siglo del Hombre dichas cantidades.'''

    sheet.cell(row=endRecord,column= 5 if isUEX else 4,value=text)
    sheet.row_dimensions[endRecord].height = 150