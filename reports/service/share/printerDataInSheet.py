def printerDataInSheet(dataTuples, startRow, startCol, sheet): 
    for rowIndex, rowData in enumerate(dataTuples, start=startRow):
        for colIndex, value in enumerate(rowData, start=startCol):
            sheet.cell(row=rowIndex, column=colIndex, value=value)
  
