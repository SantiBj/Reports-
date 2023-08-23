from ..share.calculatedTotalRecord import totalRecord


def formaterDataCoeditions(dataCoeditions):
    records = {}
    coeditorsCodCli = {}

    for record in dataCoeditions:
        coeditor = str(record["NUM"]).strip()
        totals = totalRecord(record)
        codCli = str(record["CODCLI"]).strip()

        if len(codCli) == 0:
            if not coeditor in records:
                records[coeditor] = [{
                    "CODIGO": str(record["CODIGO"]).strip(),
                    "TIPO":str(record["TIPO"]).strip(),
                    "TITULO":str(record["TITULO"]).strip(),
                    "EDICION":str(record["EDICION"]).strip(),
                    "AUTOR":str(record["AUTOR"]).strip(),
                    "PRECIO":str(record["PRECIO"]),
                    "CANTIDAD":str(record["CANTIDAD"]).strip(),
                    "VALOR_BRUTO":totals["grossTotal"],
                    "DESCUENTO":record["DESCTO"],
                    "VALOR_NETO":totals["netTotal"],
                    "ISBN":str(record["ISBN"]),
                    "MONEDA":str(record["MONEDA"]).strip(),
                    "COEDITOR": str(record["PROVEEDOR"]).strip(),
                }]
            else:
                oldRecordsCoeditor = records[coeditor]
                records[coeditor] = [
                    *oldRecordsCoeditor,
                    {
                        "CODIGO": str(record["CODIGO"]).strip(),
                        "TIPO":str(record["TIPO"]).strip(),
                        "TITULO":str(record["TITULO"]).strip(),
                        "EDICION":str(record["EDICION"]).strip(),
                        "AUTOR":str(record["AUTOR"]).strip(),
                        "PRECIO":str(record["PRECIO"]),
                        "CANTIDAD":str(record["CANTIDAD"]).strip(),
                        "VALOR_BRUTO":totals["grossTotal"],
                        "DESCUENTO":record["DESCTO"],
                        "ISBN":str(record["ISBN"]),
                        "VALOR_NETO":totals["netTotal"],
                        "MONEDA":str(record["MONEDA"]).strip(),
                        "COEDITOR": str(record["PROVEEDOR"]).strip(),
                    }
                ]
        else:
            if not codCli in coeditorsCodCli:
                coeditorsCodCli[codCli] = {}
                coeditorsCodCli[codCli][coeditor] = [{
                        "CODIGO": str(record["CODIGO"]).strip(),
                        "TIPO":str(record["TIPO"]).strip(),
                        "TITULO":str(record["TITULO"]).strip(),
                        "EDICION":str(record["EDICION"]).strip(),
                        "AUTOR":str(record["AUTOR"]).strip(),
                        "PRECIO":str(record["PRECIO"]),
                        "CANTIDAD":str(record["CANTIDAD"]).strip(),
                        "VALOR_BRUTO":totals["grossTotal"],
                        "DESCUENTO":record["DESCTO"],
                        "ISBN":str(record["ISBN"]),
                        "VALOR_NETO":totals["netTotal"],
                        "MONEDA":str(record["MONEDA"]).strip(),
                        "COEDITOR": str(record["PROVEEDOR"]).strip(),
                    }]
            elif codCli in coeditorsCodCli and not coeditor in coeditorsCodCli[codCli]:
                coeditorsCodCli[codCli][coeditor] = [{
                    "CODIGO": str(record["CODIGO"]).strip(),
                    "TIPO":str(record["TIPO"]).strip(),
                    "TITULO":str(record["TITULO"]).strip(),
                    "EDICION":str(record["EDICION"]).strip(),
                    "AUTOR":str(record["AUTOR"]).strip(),
                    "PRECIO":str(record["PRECIO"]),
                    "CANTIDAD":str(record["CANTIDAD"]).strip(),
                    "VALOR_BRUTO":totals["grossTotal"],
                    "DESCUENTO":record["DESCTO"],
                    "ISBN":str(record["ISBN"]),
                    "VALOR_NETO":totals["netTotal"],
                    "MONEDA":str(record["MONEDA"]).strip(),
                    "COEDITOR": str(record["PROVEEDOR"]).strip()
                }]

                
            elif codCli in coeditorsCodCli and coeditor in coeditorsCodCli[codCli]:
                coeditorsCodCli[codCli][coeditor] = [
                    *coeditorsCodCli[codCli][coeditor],
                    {
                        "CODIGO": str(record["CODIGO"]).strip(),
                        "TIPO":str(record["TIPO"]).strip(),
                        "TITULO":str(record["TITULO"]).strip(),
                        "EDICION":str(record["EDICION"]).strip(),
                        "AUTOR":str(record["AUTOR"]).strip(),
                        "PRECIO":str(record["PRECIO"]),
                        "CANTIDAD":str(record["CANTIDAD"]).strip(),
                        "VALOR_BRUTO":totals["grossTotal"],
                        "DESCUENTO":record["DESCTO"],
                        "ISBN":str(record["ISBN"]),
                        "VALOR_NETO":totals["netTotal"],
                        "MONEDA":str(record["MONEDA"]).strip(),
                        "COEDITOR": str(record["PROVEEDOR"]).strip(),
                    }
                ]

    return {
        "records": records,
        "coeditorsCodCli": coeditorsCodCli
    }
