# import nltk
# from fuzzywuzzy import fuzz
# from fuzzywuzzy import process

def fileValidation(text):
    # nltk.download('punkt')
    if text is None:
        return None
    # words = nltk.word_tokenizer(text)
    isValid = False
    # validKeywords = ['Customer ID', 'Name', 'Account Number', 'Garnishment Status', 'Garnishment Type', 'Garnishment Amount', 'Court Information', 'Garnishment Details']
    validKeywords = ['customerid', 'customer id', 'customer-id', 'account number','account no.', 'account no', 'account num','garnishment']
    for word in validKeywords:
        if word in text.lower():
            isValid = True
    if isValid == False:
        return "Invalid"
    return "Valid"
