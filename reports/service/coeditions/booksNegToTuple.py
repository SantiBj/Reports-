from .fromDictToTuple import formatedFromDictToTuple

def booksNegToTuple(books,hasSap):
    tuplesNegatives = []
    for bookNegative in books['books']:
        tuplesNegatives.append(formatedFromDictToTuple(bookNegative,hasSap))
    return tuplesNegatives