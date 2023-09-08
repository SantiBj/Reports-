from openpyxl.styles import PatternFill
def resaltDta(sheet,hasSap,endRecord):
    cells = [f'A{endRecord}', f'B{endRecord}', f'C{endRecord}', f'D{endRecord}', f'E{endRecord}', f'F{endRecord}',
            f'G{endRecord}', f'H{endRecord}', f'I{endRecord}', f'J{endRecord}', f'K{endRecord}']
    if hasSap:
        cells.append(f'L{endRecord}')
    for cll in cells:
        sheet[cll].fill = PatternFill(start_color="cccccc",
                                    end_color="cccccc", fill_type="solid")