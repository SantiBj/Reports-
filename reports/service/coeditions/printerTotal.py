def printerTotal(sheet, totals, hasSap):
    endRowInSheet = sheet.max_row+2
    if hasSap:
        sheet.cell(row=endRowInSheet, column=7, value="Total libros sin devoluciones :")
        sheet.cell(row=endRowInSheet, column=8,
                   value=totals["totalQuantity"])
        sheet.cell(row=endRowInSheet, column=9,
                   value=totals["totalGrossValue"])
        sheet.cell(row=endRowInSheet, column=11,
                   value=totals["totalNetValue"])
    else:
        sheet.cell(row=endRowInSheet, column=6, value="Total libros sin devoluciones :")
        sheet.cell(row=endRowInSheet, column=7,
                   value=totals["totalQuantity"])
        sheet.cell(row=endRowInSheet, column=8,
                   value=totals["totalGrossValue"])
        sheet.cell(row=endRowInSheet, column=10,
                   value=totals["totalNetValue"])
