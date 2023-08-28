from django.shortcuts import render
from ..share.calculatedTotals import calculateTotalWithDataNegative, bookNegativeAndCalculationTotals, total
from datetime import datetime
from weasyprint import HTML, CSS
from django.http import HttpResponse


def createPdf(data, cutNumber, request,hasSap, codCli=False):
    if codCli:
        # para calcular totales
        dataFull = []
        dataWithNCut = []
        keysEditor = data.keys()
        for key in keysEditor:
            dataFull = [*dataFull, *data[key]]
            dataWithNCut = [
                *dataWithNCut, {
                    "key": key,
                    "dependencia": data[key][0]["COEDITOR"]
                }, *data[key]
            ]

        calculationsTotals = total(dataFull)
        booksNegative = bookNegativeAndCalculationTotals(dataFull)
        newTotal = calculateTotalWithDataNegative(
            calculationsTotals, booksNegative)
        today = datetime.now().date()
        html = render(request, "coeditors/coeditorPdf.html", {
            "records": dataWithNCut,
            "codCli": True,
            "isSAP":hasSap,
            "moneda": dataFull[0]["MONEDA"],
            "totals": calculationsTotals,
            "booksNegative": booksNegative["books"],
            "totalNeg":booksNegative,
            "hasNegatives": True if len(booksNegative["books"]) > 0 else False,
            "newsTotals": newTotal,
            "fecha": today
        }).content.decode('utf-8')

        pdf = HTML(string=html).write_pdf(
            stylesheets=[CSS(string='@page { size: landscape; }')])
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename={dataFull[0]["COEDITOR"]}.pdf'

        return response

    else:
        calculationsTotals = total(data)
        booksNegative = bookNegativeAndCalculationTotals(data)
        newTotal = calculateTotalWithDataNegative(
            calculationsTotals, booksNegative)
        today = datetime.now().date()
        html = render(request, "coeditors/coeditorPdf.html", {
            "records": data,
            "codCli": False,
            "isSAP":hasSap,
            "moneda": data[0]["MONEDA"],
            "coeditor": data[0]["COEDITOR"],
            "totals": calculationsTotals,
            "booksNegative": booksNegative["books"],
            "booksNegative": booksNegative["books"],
            "hasNegatives": True if len(booksNegative["books"]) > 0 else False,
            "newsTotals": newTotal,
            "cutNumber": cutNumber,
            "fecha": today
        }).content.decode('utf-8')

        pdf = HTML(string=html).write_pdf(
            stylesheets=[CSS(string='@page { size: landscape; }')])
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename={data[0]["COEDITOR"]}.pdf'

        return response
