def printerTotalNegatives(totalNeg, sheet, endRow, hasSap,text):
    if hasSap:
        sheet.cell(row=endRow, column=7, value=text)
        sheet.cell(row=endRow, column=8, value=totalNeg["quantity"])
        sheet.cell(row=endRow, column=9, value=totalNeg["grossTotal"])
        sheet.cell(row=endRow, column=11, value=totalNeg["netTotal"])
    else:
        sheet.cell(row=endRow, column=6, value=text)
        sheet.cell(row=endRow, column=7, value=totalNeg["quantity"])
        sheet.cell(row=endRow, column=8, value=totalNeg["grossTotal"])
        sheet.cell(row=endRow, column=10, value=totalNeg["netTotal"])
