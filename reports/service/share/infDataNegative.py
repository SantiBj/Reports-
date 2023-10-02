def createChartText(sheet, hasSap, coe=False):
    endRecord = sheet.max_row+3
    text = '''NOTA: Los valores negativos en la columna CANTIDAD\n
            corresponden a devoluciones en ventas  reportadas\n
            por nuestros clientes durante el periodo en referencia,\n
            por tanto solicitamos a ustedes se sirva expedir\n
            la correspondiente nota crédito y cargar al inventario\n
            de Siglo del Hombre dichas cantidades.'''
    
    if hasSap :
        col = 4 if coe else 5
    else:
        col = 3 if coe else 4
    
    sheet.cell(row=endRecord, column=col, value=text)
    sheet.row_dimensions[endRecord].height = 150