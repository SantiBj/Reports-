from django.shortcuts import render
from ..share.calculatedTotals import calculateTotalWithDataNegative, bookNegativeAndCalculationTotals, total
from weasyprint import HTML, CSS
from django.http import HttpResponse

    
def createPdf(data, cutNumber, request, hasSap, codCli=False):
    if codCli:
        # para calcular totales
        dataFull = []
        allBooksWithoutDev = []

        devolutions = []
        devolutionsWithCoe = {}
        devolutionsForPrint = []

        bookWithoutDevAndCoe = []
        keysEditor = list(data.keys())

        for key in keysEditor:
            dataFull = [*dataFull, *data[key]]
            bookWithoutDevAndCoe = [
                *bookWithoutDevAndCoe, {
                    "key": key,
                    "dependencia": data[key][0]["COEDITOR"]
                }, ]
            for record in data[key]:
                if record["CANTIDAD"] >= 0:
                    allBooksWithoutDev.append(record)
                    bookWithoutDevAndCoe = [
                        *bookWithoutDevAndCoe,
                        record
                    ] 
                else :
                    devolutions.append(record)
                    if key in devolutionsWithCoe:
                        devolutionsWithCoe[key] = [
                            *devolutionsWithCoe[key],
                            record
                        ]
                    else:
                        devolutionsWithCoe[key] = [record]
        
        if len(devolutionsWithCoe.keys()) > 0:
            for faculty in devolutionsWithCoe.keys():
                devolutionsForPrint = [
                    *devolutionsForPrint,
                    {
                    "key": key,
                    "dependencia": data[key][0]["COEDITOR"]
                    }
                ]
                for devolution in devolutionsWithCoe[faculty]:
                    devolutionsForPrint =  [
                        *devolutionsForPrint,
                        devolution
                     ]

        totalBooks = total(allBooksWithoutDev)
        booksDev = bookNegativeAndCalculationTotals(dataFull)
        totalN = calculateTotalWithDataNegative(totalBooks,booksDev)
        today = dataFull[0]["FECHA"]

        html = render(request, "coeditors/coeditorPdf.html", {
            "books": bookWithoutDevAndCoe,
            "codCli": True,
            "isSAP": hasSap,
            "moneda": dataFull[0]["MONEDA"],
            "maked":dataFull[0]["ELABORADO"],
            "totalsBooks": totalBooks,
            "devolutions": devolutionsForPrint,
            "totalDevolutions":booksDev,
            "total":totalN,
            "hasNegatives": True if len(booksDev["books"]) > 0 else False,
            "fecha": today
        }).content.decode('utf-8')

        dateOfFile = dataFull[0]["FECHA"].split('-')

        pdf = HTML(string=html).write_pdf(
            stylesheets=[CSS(string='''@page { size: landscape;  margin:100px; 
                         @bottom-right { content: "Página " counter(page) " de " counter(pages);font-size:10px;};
                            @bottom-center { content: "Carrera 31A No. 25B-50 Bogotá - Colombia  |  https://libreriasiglo.com/  |   e-mail: contabilidad@somossiglo.com  |  PBX: (571) 337 77 00"; font-size: 10px; }
                         ''')])
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename={dataFull[0]["COEDITOR"][4:30]}{dateOfFile[4]}_{dateOfFile[3]}_{cutNumber}.pdf'

        return response

    else:
        bookWithoutDevolutions = []

        for book in data:
            if book["CANTIDAD"] >= 0:
                bookWithoutDevolutions.append(book)

        totalBooks = total(bookWithoutDevolutions)
        totalDevolutions = bookNegativeAndCalculationTotals(data)
        totalN = calculateTotalWithDataNegative(totalBooks,totalDevolutions)
        today = data[0]["FECHA"]
        html = render(request, "coeditors/coeditorPdf.html", {
            "books": bookWithoutDevolutions,
            "codCli": False,
            "isSAP": hasSap,
            "maked":data[0]["ELABORADO"],
            "moneda": data[0]["MONEDA"],
            "coeditor": data[0]["COEDITOR"],
            "totalsBooks": totalBooks,
            "devolutions": totalDevolutions["books"],
            "totalDevolutions":totalDevolutions,
            "total":totalN,
            "hasNegatives": True if len(totalDevolutions["books"]) > 0 else False,
            "cutNumber": cutNumber,
            "fecha": today
        }).content.decode('utf-8')

        dateOfFile = data[0]["FECHA"].split('-')

        pdf = HTML(string=html).write_pdf(
            stylesheets=[CSS(string='''@page { size: landscape;  margin:100px; 
                         @bottom-right { content: "Página " counter(page) " de " counter(pages);font-size:10px;};
                            @bottom-center { content: "Carrera 31A No. 25B-50 Bogotá - Colombia  |  https://libreriasiglo.com/  |   e-mail: contabilidad@somossiglo.com  |  PBX: (571) 337 77 00"; font-size: 10px; }
                         ''')])
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename={data[0]["COEDITOR"][4:30]}{dateOfFile[4]}_{dateOfFile[3]}_{cutNumber}.pdf'

        return response
