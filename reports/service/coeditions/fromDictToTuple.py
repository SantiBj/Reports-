def formatedFromDictToTuple(dict, hasSap):
    return (
        dict["CODIGO"],
        dict["SAP"] if "SAP" in dict else "",
        dict["TIPO"],
        dict["TITULO"],
        dict["EDICION"],
        dict["AUTOR"],
        dict["PRECIO"],
        dict["CANTIDAD"],
        dict["VALOR_BRUTO"],
        dict["DESCUENTO"],
        dict["VALOR_NETO"]
    )if hasSap else (
        dict["CODIGO"],
        dict["TIPO"],
        dict["TITULO"],
        dict["EDICION"],
        dict["AUTOR"],
        dict["PRECIO"],
        dict["CANTIDAD"],
        dict["VALOR_BRUTO"],
        dict["DESCUENTO"],
        dict["VALOR_NETO"]
    )
