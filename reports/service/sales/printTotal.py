def printTotal(tQuantity, tGross, tNet, sheet, hasSap, endRecord,text):
    if hasSap:
        sheet.cell(row=endRecord, column=8, value=text)
        sheet.cell(row=endRecord, column=9,
                   value=tQuantity)
        sheet.cell(row=endRecord, column=10,
                   value=tGross)
        sheet.cell(row=endRecord, column=12,
                   value=tNet)
    else:
        sheet.cell(row=endRecord, column=7, value=text)
        sheet.cell(row=endRecord, column=8,
                   value=tQuantity)
        sheet.cell(row=endRecord, column=9,
                   value=tGross)
        sheet.cell(row=endRecord, column=11,
                   value=tNet)
