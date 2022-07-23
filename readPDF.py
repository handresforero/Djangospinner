import PyPDF2

file = 'Diccionario Polifuncional - Sinonimos - Antonimos - Paronimos - Uso de la Lengua Espanola.pdf'

def main():
    pdfFile = "DICCIONARIO DE SINÓNIMOS Y ANTÓNIMOS – Espasa.pdf"
    pdfRead = PyPDF2.PdfFileReader(pdfFile)
    
    page = pdfRead.getPage(4    )
    pageContent = page.extractText().encode('utf-8')
    print(pageContent)

if __name__== "__main__":
    main()
