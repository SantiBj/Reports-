from dbfread import DBF
import tempfile
from decimal import Decimal,getcontext

# separacion de miles
# redondeo a 2 posiciones
# manual tecnico 
# manual de usuario


def transform(fileInserted):
    records = {}
    # create temporal file
    with tempfile.NamedTemporaryFile(delete=False) as fileTemp:
        fileTemp.write(fileInserted.read())

        with DBF(fileTemp.name, encoding='cp850') as tableOfFile:
            # recorro los datos del archivo
            for recordTable in tableOfFile:
                grossValue = Decimal(
                    recordTable["PRECIO"]) * int(recordTable["CANTIDAD"])
                discountInMoneyForGrossValue = grossValue * \
                    (Decimal(recordTable["DESCTO"]) / 100)
                netValue = grossValue - discountInMoneyForGrossValue
                num = str(recordTable["NUM"]).strip()

                # valido si no esta en records
                if not num in records:
                    if str(recordTable["PROVEEDOR"]).strip()[:3] == "UEX":
                        records[num] = [{
                            "CODIGO": str(recordTable["CODIGO"]).strip(),
                            "ISBN":str(recordTable["ISBN"]).strip(),
                            "SAP":str(recordTable["SAP"]).strip(),
                            "IDBARRAS":str(recordTable["IDBARRAS"]).strip(),
                            "TITULO":str(recordTable["TITULO"]).strip(),
                            "EDICION":str(recordTable["EDICION"]).strip(),
                            "AUTOR":str(recordTable["AUTOR"]).strip(),
                            "PRECIO":recordTable["PRECIO"],
                            "CANTIDAD":int(recordTable["CANTIDAD"]),
                            "VALOR_BRUTO": grossValue,
                            "DESCUENTO":recordTable["DESCTO"],
                            "VALOR_NETO":netValue,
                            "MONEDA":str(recordTable["MONEDA"]).strip(),
                            "PROVEEDOR":str(recordTable["PROVEEDOR"]).strip(),
                        }]
                    else:
                        records[num] = [{
                            "CODIGO": str(recordTable["CODIGO"]).strip(),
                            "ISBN":str(recordTable["ISBN"]).strip(),
                            "IDBARRAS":str(recordTable["IDBARRAS"]).strip(),
                            "TITULO":str(recordTable["TITULO"]).strip(),
                            "EDICION":str(recordTable["EDICION"]).strip(),
                            "AUTOR":str(recordTable["AUTOR"]).strip(),
                            "PRECIO":recordTable["PRECIO"],
                            "CANTIDAD":int(recordTable["CANTIDAD"]),
                            "VALOR_BRUTO": grossValue,
                            "DESCUENTO":recordTable["DESCTO"],
                            "VALOR_NETO":netValue,
                            "MONEDA":str(recordTable["MONEDA"]).strip(),
                            "PROVEEDOR":str(recordTable["PROVEEDOR"]).strip(),
                        }]

                else:
                    dataKey = records[num]

                    if str(recordTable["PROVEEDOR"]).strip()[:3] == "UEX":
                        records[num] = [
                            *dataKey,
                            {
                                "CODIGO": str(recordTable["CODIGO"]).strip(),
                                "ISBN":str(recordTable["ISBN"]).strip(),
                                "SAP":str(recordTable["SAP"]).strip(),
                                "IDBARRAS":str(recordTable["IDBARRAS"]).strip(),
                                "TITULO":str(recordTable["TITULO"]).strip(),
                                "EDICION":str(recordTable["EDICION"]).strip(),
                                "AUTOR":str(recordTable["AUTOR"]).strip(),
                                "PRECIO":recordTable["PRECIO"],
                                "CANTIDAD":int(recordTable["CANTIDAD"]),
                                "VALOR_BRUTO": grossValue,
                                "DESCUENTO":recordTable["DESCTO"],
                                "VALOR_NETO":netValue,
                                "MONEDA":str(recordTable["MONEDA"]).strip(),
                                "PROVEEDOR":str(recordTable["PROVEEDOR"]).strip(),
                            }
                        ]
                    else:
                        records[num] = [
                            *dataKey,
                            {
                                "CODIGO": str(recordTable["CODIGO"]).strip(),
                                "ISBN":str(recordTable["ISBN"]).strip(),
                                "IDBARRAS":str(recordTable["IDBARRAS"]).strip(),
                                "TITULO":str(recordTable["TITULO"]).strip(),
                                "EDICION":str(recordTable["EDICION"]).strip(),
                                "AUTOR":str(recordTable["AUTOR"]).strip(),
                                "PRECIO":recordTable["PRECIO"],
                                "CANTIDAD":int(recordTable["CANTIDAD"]),
                                "VALOR_BRUTO": grossValue,
                                "DESCUENTO":recordTable["DESCTO"],
                                "VALOR_NETO":netValue,
                                "MONEDA":str(recordTable["MONEDA"]).strip(),
                                "PROVEEDOR":str(recordTable["PROVEEDOR"]).strip(),
                            }
                        ]

    return records
