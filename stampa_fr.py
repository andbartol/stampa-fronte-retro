from PyPDF2 import PdfFileReader, PdfFileWriter
import sys

if len(sys.argv) < 3:
    print "Usage: python " + sys.argv[0] + " input.pdf output.pdf"
    exit(1)

with open(sys.argv[1], "rb") as input:
    pdfInput = PdfFileReader(input)
    nPages = pdfInput.getNumPages()
    pari = PdfFileWriter()
    dispari = PdfFileWriter()
    for i in range(nPages):
        if i%2==0:
            pari.addPage(pdfInput.getPage(i))
        else:
            dispari.addPage(pdfInput.getPage(i))
    nPages = dispari.getNumPages()
    for i in range(nPages):
        pari.addPage(dispari.getPage(i))
    with open(sys.argv[2], "wb") as out:
        pari.write(out)
