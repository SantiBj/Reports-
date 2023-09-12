from ..sales.formatedRecordForDictToTuple import formatedRecordForDictToTuple
from ..sales.resaltData import resaltDta
from ..sales.printTotal import printTotal

# suma total bruto, total neto y cantidad de todos los libros del proveedor


def total(recordsSupplier):
    totalQuantity = 0
    totalGrossValue = 0
    totalNetValue = 0

    for record in recordsSupplier:
        totalQuantity += int(record["CANTIDAD"])
        totalGrossValue += record["VALOR_BRUTO"]
        totalNetValue += record["VALOR_NETO"]

    return {
        "totalQuantity": totalQuantity,
        "totalGrossValue": totalGrossValue,
        "totalNetValue": totalNetValue,
    }

# sales


def printerTotalBooksAndDevolutions(booksPositives, allBooks, sheet, isUEX):
    totalPositives = total(booksPositives)
    endRecord = sheet.max_row+2

    # total libros sin devoluciones
    resaltDta(sheet, isUEX, endRecord)
    printTotal(totalPositives["totalQuantity"], totalPositives["totalGrossValue"],
               totalPositives["totalNetValue"], sheet, isUEX, endRecord, "Total libros sin devoluciones :")

    # devoluciones libros
    endRecord = sheet.max_row+3
    bookNegative = bookNegativeAndCalculationTotals(allBooks)

    if len(bookNegative["books"]) > 0:
        booksWithQuantityNegativeTuple = []

        # añadiendo las devoluciones a una tupla
        for book in bookNegative["books"]:
            booksWithQuantityNegativeTuple.append(
                formatedRecordForDictToTuple(book, isUEX))

        # pintando en el excel las devoluciones
        for rowIndex, rowData in enumerate(booksWithQuantityNegativeTuple, start=endRecord):
            for colIndex, value in enumerate(rowData, start=1):
                sheet.cell(row=rowIndex, column=colIndex, value=value)

        endRecord = sheet.max_row+1
        # pintando el total de devoluciones
        resaltDta(sheet, isUEX, endRecord)
        printTotal(bookNegative["quantity"], bookNegative["grossTotal"],
                   bookNegative["netTotal"], sheet, isUEX, endRecord, "total devoluciones : ")
        endRecord = sheet.max_row+2

        # calculando y pintando el total de libros y devoluciones
        endTotal = calculateTotalWithDataNegative(totalPositives, bookNegative)
        resaltDta(sheet, isUEX, endRecord)
        printTotal(endTotal["quantity"], endTotal["grossTotal"],
                   endTotal["netTotal"], sheet, isUEX, endRecord, "Total : ")

    # memsaje que indica el signifiado de las catidades negativas
    if len(bookNegative["books"]) > 0:
        createChartText(sheet, isUEX)


# suma de libros con devoluciones
def calculateTotalWithDataNegative(total, totalNegatives):
    return {
        "quantity": total["totalQuantity"]+totalNegatives["quantity"],
        "grossTotal": total["totalGrossValue"]+totalNegatives["grossTotal"],
        "netTotal": total["totalNetValue"]+totalNegatives["netTotal"],
    }

# lista de devoluciones y calculo de los totales de estas


def bookNegativeAndCalculationTotals(recordsSupplier):
    booksWithQuantityNegative = []
    totalQuantityNegatives = 0
    totalGrossNegatives = 0
    totalNetNegatives = 0

    for recordT in recordsSupplier:
        if int(recordT["CANTIDAD"]) < 0:
            totalQuantityNegatives += int(recordT["CANTIDAD"])
            totalGrossNegatives += recordT["VALOR_BRUTO"]
            totalNetNegatives += recordT["VALOR_NETO"]
            booksWithQuantityNegative.append(recordT)
    return {
        "books": booksWithQuantityNegative,
        "quantity": totalQuantityNegatives,
        "grossTotal": totalGrossNegatives,
        "netTotal": totalNetNegatives
    }


def createChartText(sheet, isUEX):
    endRecord = sheet.max_row+3
    text = '''NOTA: Los valores negativos en la columna CANTIDAD\n
            corresponden a devoluciones en ventas  reportadas\n
            por nuestros clientes durante el periodo en referencia,\n
            por tanto solicitamos a ustedes se sirva expedir\n
            la correspondiente nota crédito y cargar al inventario\n
            de Siglo del Hombre dichas cantidades.'''

    sheet.cell(row=endRecord, column=5 if isUEX else 4, value=text)
    sheet.row_dimensions[endRecord].height = 150
