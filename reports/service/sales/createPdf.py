from django.shortcuts import render
from django.http import HttpResponse
from .bookWithoutDevolutions import bookWithoutDevolutions
from ..share.calculatedTotals import calculateTotalWithDataNegative, total, bookNegativeAndCalculationTotals
from weasyprint import HTML, CSS


# sacar total en un service
# sacar calculate

def createPdf(data, supplier, request, hasSap):
    # content pdf
    booksWithoutDevolutions = bookWithoutDevolutions(data, hasSap)
    Tbooks = total(booksWithoutDevolutions["booksDict"])
    booksNegative = bookNegativeAndCalculationTotals(data)
    totalN = calculateTotalWithDataNegative(Tbooks, booksNegative)
    # pasando el tipo de monedad para realizar validaciones en la plantilla

    html = render(request, 'reports/reportPdf.html', {
        "books": booksWithoutDevolutions["booksDict"],
        "moneda": data[0]["MONEDA"],
        "proveedor": data[0]["PROVEEDOR"],
        "maked": data[0]["ELABORADO"],
        "isSAP": hasSap,
        "Tbooks": Tbooks,
        "devolutions": booksNegative,
        "hasNegatives":  True if len(booksNegative["books"]) > 0 else False,
        "cutNumber": supplier,
        "total": totalN,
        "fecha": data[0]["FECHA"]
    }).content.decode('utf-8')

    # return html
    html = HTML(string=html)
    css = CSS(string='''@page { size: landscape;  margin:100px; 
                         @bottom-right { content: "Página " counter(page) " de " counter(pages);font-size:10px;};
                            @bottom-center { content: "Carrera 31A No. 25B-50 Bogotá - Colombia  |  https://libreriasiglo.com/  |   e-mail: contabilidad@somossiglo.com  |  PBX: (571) 337 77 00"; font-size: 10px; }
                         ''')
    
    pdf = html.write_pdf(stylesheets=[css])

    date = data[0]["FECHA"].split('-')

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename={data[0]["PROVEEDOR"][:3]}{date[4]}_{date[3]}.pdf'

    return response
