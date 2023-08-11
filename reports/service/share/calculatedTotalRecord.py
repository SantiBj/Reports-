from decimal import Decimal

def totalRecord(record):
    grossTotal = Decimal(record["PRECIO"]) * Decimal(record["CANTIDAD"])
    totalDiscount = grossTotal * (Decimal(record["DESCTO"]) / 100)
    netTotal = grossTotal - totalDiscount 

    return {
        "grossTotal": grossTotal,
        "netTotal":netTotal
    }