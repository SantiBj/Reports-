def formatedFromDictToTuple(dict):
    return (
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
