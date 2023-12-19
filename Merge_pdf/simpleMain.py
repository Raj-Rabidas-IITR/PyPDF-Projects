from PyPDF2 import PdfWriter
#Support link to learn  : https://pypdf.readthedocs.io/en/stable/
import os

#creating an object for writing

merger=PdfWriter()

files=[file for file in os.listdir() if file.endswith(".pdf")]


for pdf in files:
    merger.append(pdf) #this is the method to merged the pdf files one by one


merger.write("Merged-pdf2.pdf")
#close the writer object
merger.close()

