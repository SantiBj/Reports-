def formatedFromDictToTuple(dict):
    return (
        dict["CODIGO"],
        dict["TIPO"],
        dict["TITULO"],
        dict["EDICION"],
        dict["AUTOR"],
        dict["PRECIO"],
        dict["CANTIDAD"],
        dict["TOTAL_BRUTO"],
        dict["DESCUENTO"],
        dict["TOTAL_NETO"]
    )
