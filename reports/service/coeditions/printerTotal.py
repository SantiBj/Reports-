def printerTotal(sheet, totals):
    endRowInSheet = sheet.max_row+2
    sheet.cell(row=endRowInSheet, column=6, value="Total = ")
    sheet.cell(row=endRowInSheet, column=7,
               value=totals["totalQuantity"])
    sheet.cell(row=endRowInSheet, column=8,
               value=totals["totalGrossValue"])
    sheet.cell(row=endRowInSheet, column=10,
               value=totals["totalNetValue"])
