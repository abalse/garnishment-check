from PyPDF2 import PdfReader

def pdfReader(fileName):
    print(fileName)
    print(type(fileName))
    if fileName is None:
        return None
    
    reader = PdfReader(fileName)
    pageNum = 0
    text = ''
    while 1:
        try:
            page = reader.pages[pageNum]
            text = text + '\n' + page.extract_text()
            pageNum += 1
        except:
            break
    return text