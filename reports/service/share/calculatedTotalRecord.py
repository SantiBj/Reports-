from decimal import Decimal
def totalRecord(record):
    grossTotal = record["PRECIO"] * record["CANTIDAD"]
    totalDiscount = grossTotal * (record["DESCTO"] / 100)
    netTotal = grossTotal - totalDiscount 


    return {
        "grossTotal": round(Decimal(grossTotal),2),
        "netTotal":round(Decimal(netTotal),2)
    }