from ..share.calculatedTotalRecord import totalRecord

# separacion de miles
# redondeo a 2 posiciones
# manual tecnico 
# manual de usuario


def formatterDataSales(dataSales):
    records = {}

    # recorro los datos del archivo
    for recordSale in dataSales:
        totals = totalRecord(recordSale)
        num = str(recordSale["NUM"]).strip()

        # valido si no esta en records
        if not num in records:
            if len(str(recordSale["SAP"]).strip()) == 0:
                records[num] = [{
                    "CODIGO": str(recordSale["CODIGO"]).strip(),
                    "FECHA":f"{str(recordSale['DESDE']).strip()} / {str(recordSale['HASTA']).strip()}",
                    "ISBN":str(recordSale["ISBN"]).strip(),
                    "IDBARRAS":str(recordSale["IDBARRAS"]).strip(),
                    "TITULO":str(recordSale["TITULO"]).strip(),
                    "EDICION":str(recordSale["EDICION"]).strip(),
                    "AUTOR":str(recordSale["AUTOR"]).strip(),
                    "PRECIO":recordSale["PRECIO"],
                    "CANTIDAD":int(recordSale["CANTIDAD"]),
                    "VALOR_BRUTO": totals["grossTotal"],
                    "DESCUENTO":recordSale["DESCTO"],
                    "VALOR_NETO":totals["netTotal"],
                    "MONEDA":str(recordSale["MONEDA"]).strip(),
                    "PROVEEDOR":str(recordSale["PROVEEDOR"]).strip(),
                }]
            else:
                records[num] = [{
                    "CODIGO": str(recordSale["CODIGO"]).strip(),
                    "FECHA":f"{str(recordSale['DESDE']).strip()}-{str(recordSale['HASTA']).strip()}",
                    "ISBN":str(recordSale["ISBN"]).strip(),
                    "IDBARRAS":str(recordSale["IDBARRAS"]).strip(),
                    "TITULO":str(recordSale["TITULO"]).strip(),
                    "EDICION":str(recordSale["EDICION"]).strip(),
                    "AUTOR":str(recordSale["AUTOR"]).strip(),
                    "SAP":str(recordSale["SAP"]).strip(),
                    "PRECIO":recordSale["PRECIO"],
                    "CANTIDAD":int(recordSale["CANTIDAD"]),
                    "VALOR_BRUTO": totals["grossTotal"],
                    "DESCUENTO":recordSale["DESCTO"],
                    "VALOR_NETO":totals["netTotal"],
                    "MONEDA":str(recordSale["MONEDA"]).strip(),
                    "PROVEEDOR":str(recordSale["PROVEEDOR"]).strip(),
                }]

        else:
            dataKey = records[num]

            if str(recordSale["PROVEEDOR"]).strip()[:3] == "UEX":
                records[num] = [
                    *dataKey,
                    {
                        "CODIGO": str(recordSale["CODIGO"]).strip(),
                        "FECHA":f"{str(recordSale['DESDE']).strip()}-{str(recordSale['HASTA']).strip()}",
                        "ISBN":str(recordSale["ISBN"]).strip(),
                        "SAP":str(recordSale["SAP"]).strip(),
                        "IDBARRAS":str(recordSale["IDBARRAS"]).strip(),
                        "TITULO":str(recordSale["TITULO"]).strip(),
                        "EDICION":str(recordSale["EDICION"]).strip(),
                        "AUTOR":str(recordSale["AUTOR"]).strip(),
                        "PRECIO":recordSale["PRECIO"],
                        "CANTIDAD":int(recordSale["CANTIDAD"]),
                        "VALOR_BRUTO": totals["grossTotal"],
                        "DESCUENTO":recordSale["DESCTO"],
                        "VALOR_NETO": totals["netTotal"],
                        "MONEDA":str(recordSale["MONEDA"]).strip(),
                        "PROVEEDOR":str(recordSale["PROVEEDOR"]).strip(),
                    }
                ]
            else:
                records[num] = [
                    *dataKey,
                    {
                        "CODIGO": str(recordSale["CODIGO"]).strip(),
                        "FECHA":f"{str(recordSale['DESDE']).strip()}-{str(recordSale['HASTA']).strip()}",
                        "ISBN":str(recordSale["ISBN"]).strip(),
                        "IDBARRAS":str(recordSale["IDBARRAS"]).strip(),
                        "TITULO":str(recordSale["TITULO"]).strip(),
                        "EDICION":str(recordSale["EDICION"]).strip(),
                        "AUTOR":str(recordSale["AUTOR"]).strip(),
                        "PRECIO":recordSale["PRECIO"],
                        "CANTIDAD":int(recordSale["CANTIDAD"]),
                        "VALOR_BRUTO": totals["grossTotal"],
                        "DESCUENTO":recordSale["DESCTO"],
                        "VALOR_NETO":totals["netTotal"],
                        "MONEDA":str(recordSale["MONEDA"]).strip(),
                        "PROVEEDOR":str(recordSale["PROVEEDOR"]).strip(),
                    }
                ]

    return records
