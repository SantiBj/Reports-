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
                if len(str(record["SAP"]).strip()) == 0:
                    records[coeditor] = [{
                        "CODIGO": str(record["CODIGO"]).strip(),
                        "TIPO":str(record["TIPO"]).strip(),
                        "FECHA":f"{str(record['DESDE']).strip()} - {str(record['HASTA']).strip()}",
                        "TITULO":str(record["TITULO"]).strip(),
                        "EDICION":str(record["EDICION"]).strip(),
                        "AUTOR":str(record["AUTOR"]).strip(),
                        "ELABORADO":str(record['ELABORADO']).strip(),
                        "PRECIO":record["PRECIO"],
                        "CANTIDAD":int(record["CANTIDAD"]),
                        "VALOR_BRUTO":totals["grossTotal"],
                        "DESCUENTO":record["DESCTO"],
                        "VALOR_NETO":totals["netTotal"],
                        "ISBN":str(record["ISBN"]),
                        "MONEDA":str(record["MONEDA"]).strip(),
                        "COEDITOR": str(record["PROVEEDOR"]).strip(),
                    }]
                else:
                    records[coeditor] = [{
                        "CODIGO": str(record["CODIGO"]).strip(),
                        "FECHA":f"{str(record['DESDE']).strip()} - {str(record['HASTA']).strip()}",
                        "TIPO":str(record["TIPO"]).strip(),
                        "SAP":str(record["SAP"]).strip(),
                        "TITULO":str(record["TITULO"]).strip(),
                        "ELABORADO":str(record['ELABORADO']).strip(),
                        "EDICION":str(record["EDICION"]).strip(),
                        "AUTOR":str(record["AUTOR"]).strip(),
                        "PRECIO":record["PRECIO"],
                        "CANTIDAD":int(record["CANTIDAD"]),
                        "VALOR_BRUTO":totals["grossTotal"],
                        "DESCUENTO":record["DESCTO"],
                        "VALOR_NETO":totals["netTotal"],
                        "ISBN":str(record["ISBN"]),
                        "MONEDA":str(record["MONEDA"]).strip(),
                        "COEDITOR": str(record["PROVEEDOR"]).strip(),
                    }]
            else:
                oldRecordsCoeditor = records[coeditor]
                if len(str(record["SAP"]).strip()) == 0:
                    records[coeditor] = [
                        *oldRecordsCoeditor,
                        {
                            "CODIGO": str(record["CODIGO"]).strip(),
                            "FECHA":f"{str(record['DESDE']).strip()} - {str(record['HASTA']).strip()}",
                            "TIPO":str(record["TIPO"]).strip(),
                            "TITULO":str(record["TITULO"]).strip(),
                            "ELABORADO":str(record['ELABORADO']).strip(),
                            "EDICION":str(record["EDICION"]).strip(),
                            "AUTOR":str(record["AUTOR"]).strip(),
                            "PRECIO":record["PRECIO"],
                            "CANTIDAD":int(record["CANTIDAD"]),
                            "VALOR_BRUTO":totals["grossTotal"],
                            "DESCUENTO":record["DESCTO"],
                            "ISBN":str(record["ISBN"]),
                            "VALOR_NETO":totals["netTotal"],
                            "MONEDA":str(record["MONEDA"]).strip(),
                            "COEDITOR": str(record["PROVEEDOR"]).strip(),
                        }
                    ]
                else:
                    records[coeditor] = [
                        *oldRecordsCoeditor,
                        {
                            "CODIGO": str(record["CODIGO"]).strip(),
                            "FECHA":f"{str(record['DESDE']).strip()} - {str(record['HASTA']).strip()}",
                            "TIPO":str(record["TIPO"]).strip(),
                            "TITULO":str(record["TITULO"]).strip(),
                            "EDICION":str(record["EDICION"]).strip(),
                            "ELABORADO":str(record['ELABORADO']).strip(),
                            "AUTOR":str(record["AUTOR"]).strip(),
                            "PRECIO":record["PRECIO"],
                            "CANTIDAD":int(record["CANTIDAD"]),
                            "VALOR_BRUTO":totals["grossTotal"],
                            "DESCUENTO":record["DESCTO"],
                            "ISBN":str(record["ISBN"]),
                            "SAP":str(record["SAP"]).strip(),
                            "VALOR_NETO":totals["netTotal"],
                            "MONEDA":str(record["MONEDA"]).strip(),
                            "COEDITOR": str(record["PROVEEDOR"]).strip(),
                        }
                    ]

        else:
            if not codCli in coeditorsCodCli:
                coeditorsCodCli[codCli] = {}
                if len(str(record["SAP"]).strip()) == 0:
                    coeditorsCodCli[codCli][coeditor] = [{
                        "CODIGO": str(record["CODIGO"]).strip(),
                        "FECHA":f"{str(record['DESDE']).strip()} - {str(record['HASTA']).strip()}",
                        "TIPO":str(record["TIPO"]).strip(),
                        "TITULO":str(record["TITULO"]).strip(),
                        "EDICION":str(record["EDICION"]).strip(),
                        "ELABORADO":str(record['ELABORADO']).strip(),
                        "AUTOR":str(record["AUTOR"]).strip(),
                        "PRECIO":record["PRECIO"],
                        "CANTIDAD":int(record["CANTIDAD"]),
                        "VALOR_BRUTO":totals["grossTotal"],
                        "DESCUENTO":record["DESCTO"],
                        "ISBN":str(record["ISBN"]),
                        "VALOR_NETO":totals["netTotal"],
                        "MONEDA":str(record["MONEDA"]).strip(),
                        "COEDITOR": str(record["PROVEEDOR"]).strip(),
                    }]
                else:
                    coeditorsCodCli[codCli][coeditor] = [{
                        "CODIGO": str(record["CODIGO"]).strip(),
                        "FECHA":f"{str(record['DESDE']).strip()} - {str(record['HASTA']).strip()}",
                        "TIPO":str(record["TIPO"]).strip(),
                        "TITULO":str(record["TITULO"]).strip(),
                        "EDICION":str(record["EDICION"]).strip(),
                        "AUTOR":str(record["AUTOR"]).strip(),
                        "ELABORADO":str(record['ELABORADO']).strip(),
                        "PRECIO":record["PRECIO"],
                        "CANTIDAD":int(record["CANTIDAD"]),
                        "VALOR_BRUTO":totals["grossTotal"],
                        "DESCUENTO":record["DESCTO"],
                        "ISBN":str(record["ISBN"]),
                        "SAP":str(record["SAP"]).strip(),
                        "VALOR_NETO":totals["netTotal"],
                        "MONEDA":str(record["MONEDA"]).strip(),
                        "COEDITOR": str(record["PROVEEDOR"]).strip(),
                    }]
            elif codCli in coeditorsCodCli and not coeditor in coeditorsCodCli[codCli]:
                if len(str(record["SAP"]).strip()) == 0:
                    coeditorsCodCli[codCli][coeditor] = [{
                        "CODIGO": str(record["CODIGO"]).strip(),
                        "FECHA":f"{str(record['DESDE']).strip()} - {str(record['HASTA']).strip()}",
                        "TIPO":str(record["TIPO"]).strip(),
                        "TITULO":str(record["TITULO"]).strip(),
                        "ELABORADO":str(record['ELABORADO']).strip(),
                        "EDICION":str(record["EDICION"]).strip(),
                        "AUTOR":str(record["AUTOR"]).strip(),
                        "PRECIO":record["PRECIO"],
                        "CANTIDAD":int(record["CANTIDAD"]),
                        "VALOR_BRUTO":totals["grossTotal"],
                        "DESCUENTO":record["DESCTO"],
                        "ISBN":str(record["ISBN"]),
                        "VALOR_NETO":totals["netTotal"],
                        "MONEDA":str(record["MONEDA"]).strip(),
                        "COEDITOR": str(record["PROVEEDOR"]).strip()
                    }]
                else:
                    coeditorsCodCli[codCli][coeditor] = [{
                        "CODIGO": str(record["CODIGO"]).strip(),
                        "FECHA":f"{str(record['DESDE']).strip()} - {str(record['HASTA']).strip()}",
                        "TIPO":str(record["TIPO"]).strip(),
                        "TITULO":str(record["TITULO"]).strip(),
                        "EDICION":str(record["EDICION"]).strip(),
                        "ELABORADO":str(record['ELABORADO']).strip(),
                        "AUTOR":str(record["AUTOR"]).strip(),
                        "PRECIO":record["PRECIO"],
                        "CANTIDAD":int(record["CANTIDAD"]),
                        "VALOR_BRUTO":totals["grossTotal"],
                        "DESCUENTO":record["DESCTO"],
                        "ISBN":str(record["ISBN"]),
                        "SAP":str(record["SAP"]).strip(),
                        "VALOR_NETO":totals["netTotal"],
                        "MONEDA":str(record["MONEDA"]).strip(),
                        "COEDITOR": str(record["PROVEEDOR"]).strip()
                    }]

            elif codCli in coeditorsCodCli and coeditor in coeditorsCodCli[codCli]:
                if len(str(record["SAP"]).strip()) == 0:
                    coeditorsCodCli[codCli][coeditor] = [
                        *coeditorsCodCli[codCli][coeditor],
                        {
                            "CODIGO": str(record["CODIGO"]).strip(),
                            "FECHA":f"{str(record['DESDE']).strip()} - {str(record['HASTA']).strip()}",
                            "TIPO":str(record["TIPO"]).strip(),
                            "TITULO":str(record["TITULO"]).strip(),
                            "EDICION":str(record["EDICION"]).strip(),
                            "AUTOR":str(record["AUTOR"]).strip(),
                            "ELABORADO":str(record['ELABORADO']).strip(),
                            "PRECIO":record["PRECIO"],
                            "CANTIDAD":int(record["CANTIDAD"]),
                            "VALOR_BRUTO":totals["grossTotal"],
                            "DESCUENTO":record["DESCTO"],
                            "ISBN":str(record["ISBN"]),
                            "VALOR_NETO":totals["netTotal"],
                            "MONEDA":str(record["MONEDA"]).strip(),
                            "COEDITOR": str(record["PROVEEDOR"]).strip(),
                        }
                    ]
                else:
                    coeditorsCodCli[codCli][coeditor] = [
                        *coeditorsCodCli[codCli][coeditor],
                        {
                            "CODIGO": str(record["CODIGO"]).strip(),
                            "FECHA":f"{str(record['DESDE']).strip()} - {str(record['HASTA']).strip()}",
                            "TIPO":str(record["TIPO"]).strip(),
                            "TITULO":str(record["TITULO"]).strip(),
                            "EDICION":str(record["EDICION"]).strip(),
                            "ELABORADO":str(record['ELABORADO']).strip(),
                            "AUTOR":str(record["AUTOR"]).strip(),
                            "PRECIO":record["PRECIO"],
                            "CANTIDAD":int(record["CANTIDAD"]),
                            "VALOR_BRUTO":totals["grossTotal"],
                            "DESCUENTO":record["DESCTO"],
                            "ISBN":str(record["ISBN"]),
                            "SAP":str(record["SAP"]).strip(),
                            "VALOR_NETO":totals["netTotal"],
                            "MONEDA":str(record["MONEDA"]).strip(),
                            "COEDITOR": str(record["PROVEEDOR"]).strip(),
                        }
                    ]

    return {
        "records": records,
        "coeditorsCodCli": coeditorsCodCli
    }
