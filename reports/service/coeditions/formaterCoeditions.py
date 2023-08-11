from ..share.calculatedTotalRecord import totalRecord

# return {
# "andes":[registro1,registro2]
#   }
# input = [{},{}]


def formaterDataCoeditions(dataCoeditions):
    records = {}

    for record in dataCoeditions:

        coeditor = record["NUM"]
        totals = totalRecord(record)
        if not coeditor in records:
            records[coeditor] = [{
                "CODIGO": str(record["CODIGO"]).strip(),
                "TIPO":str(record["TIPO"]).strip(),
                "TITULO":str(record["TITULO"]).strip(),
                "EDICION":str(record["EDICION"]).strip(),
                "AUTOR":str(record["AUTOR"]).strip(),
                "PRECIO":str(record["PRECIO"]),
                "CANTIDAD":str(record["CANTIDAD"]).strip(),
                "TOTAL_BRUTO":totals["grossTotal"],
                "DESCUENTO":record["DESCTO"],
                "VALOR_NETO":totals["netTotal"],
                "COEDITOR":record["COEDITOR"]
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
                    "TOTAL_BRUTO":totals["grossTotal"],
                    "DESCUENTO":record["DESCTO"],
                    "VALOR_NETO":totals["netTotal"],
                    "COEDITOR":record["COEDITOR"]
                }
            ]
    return records