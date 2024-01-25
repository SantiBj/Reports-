from .fromDictToTuple import formatedFromDictToTuple

def booksNegToTuple(books,hasSap,booksCalculate=False):
    tuplesNegatives = []
    booksToFormatter = books if booksCalculate else books['books']
    for bookNegative in booksToFormatter:
        tuplesNegatives.append(formatedFromDictToTuple(bookNegative,hasSap))
    return tuplesNegatives