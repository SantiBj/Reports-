from django.shortcuts import render
from django.http import HttpResponse
from ..share.calculatedTotals import total,bookNegativeAndCalculationTotals,calculateTotalWithDataNegative
from datetime import datetime
from weasyprint import HTML,CSS



#sacar total en un service
#sacar calculate

def createPdf(data,supplier,request,hasSap):
    #content pdf
    calculationsTotals = total(data)
    booksNegative = bookNegativeAndCalculationTotals(data)
    newTotalWithBooksNegatives = calculateTotalWithDataNegative(calculationsTotals,booksNegative)
    #pasando el tipo de monedad para realizar validaciones en la plantilla
  
    html = render(request,'reports/reportPdf.html',{
        "records":data,
        "moneda":data[0]["MONEDA"],
        "proveedor":data[0]["PROVEEDOR"],
        "isSAP": hasSap,
        "totals":calculationsTotals,
        "booksNegative":booksNegative["books"],
        "hasNegatives":  True if len(booksNegative["books"]) > 0 else False,
        "totalNeg":booksNegative,
        "newsTotals":newTotalWithBooksNegatives,
        "cutNumber":supplier,
        "fecha": data[0]["FECHA"]
    }).content.decode('utf-8')
    
    #return html
   
    pdf =HTML(string=html).write_pdf(stylesheets=[CSS(string='@page { size: landscape; }')])
    
    date = data[0]["FECHA"].split('-')

    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename={data[0]["PROVEEDOR"][:3]}-{date[4]}_{date[3]}.pdf'

    return response
    