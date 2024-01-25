from .formatedRecordForDictToTuple import formatedRecordForDictToTuple

def bookWithoutDevolutions(allBooks, hasSap):
    dataPositive = []
    dataPositiveTup = []
    for data in allBooks:
        if data["CANTIDAD"] > 0:
            dataPositive.append(data)
            dataPositiveTup.append(formatedRecordForDictToTuple(data, hasSap))

    return {
        "booksDict": dataPositive,
        "booksTup": dataPositiveTup
    }