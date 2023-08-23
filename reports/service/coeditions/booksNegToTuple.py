from .fromDictToTuple import formatedFromDictToTuple

def booksNegToTuple(books):
    tuplesNegatives = []
    for bookNegative in books['books']:
        tuplesNegatives.append(formatedFromDictToTuple(bookNegative))
    return tuplesNegatives