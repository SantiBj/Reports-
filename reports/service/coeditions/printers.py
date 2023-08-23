def printerTotalNegatives(totalNeg,sheet,endRow):
        sheet.cell(row=endRow,column=6,value="Total =")
        sheet.cell(row=endRow,column=7,value=totalNeg["quantity"])
        sheet.cell(row=endRow,column=8,value=totalNeg["grossTotal"])
        sheet.cell(row=endRow,column=10,value=totalNeg["netTotal"])
