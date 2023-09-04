def formatedRecordForDictToTuple(record, hasSap):
    return (
        record["CODIGO"],
        record["ISBN"],
        record["SAP"] if "SAP" in record else "",
        record["IDBARRAS"],
        record["TITULO"],
        record["EDICION"],
        record["AUTOR"],
        record["PRECIO"],
        record["CANTIDAD"],
        record["VALOR_BRUTO"],
        record["DESCUENTO"],
        record["VALOR_NETO"]
    ) if hasSap else (
        record["CODIGO"],
        record["ISBN"],
        record["IDBARRAS"],
        record["TITULO"],
        record["EDICION"],
        record["AUTOR"],
        record["PRECIO"],
        record["CANTIDAD"],
        record["VALOR_BRUTO"],
        record["DESCUENTO"],
        record["VALOR_NETO"])
