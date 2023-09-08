def totalRecord(record):
    grossTotal = record["PRECIO"] * record["CANTIDAD"]
    totalDiscount = grossTotal * (record["DESCTO"] / 100)
    netTotal = grossTotal - totalDiscount 

    return {
        "grossTotal": grossTotal,
        "netTotal":netTotal
    }