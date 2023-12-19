#Merging pdf files using pyPDF
#This library is very usefull

'''

pyPDF: A Python Library for Working with PDFs
pyPDF is a popular Python library for working with PDF documents. It allows you to:

    -Read and extract text from PDFs
    -Manipulate (merge, split, rotate) PDF pages
    -Add annotations and watermarks
    -Encrypt and decrypt PDFs
    -Extract metadata



'''
# This program reads the pdf and extract the text into a text file 

import PyPDF2 as p2

pdf_file=open("mdg.pdf","rb")

#Create a PDF reader obj
read_obj= p2.PdfReader(pdf_file)


# To read no of pages
pageno=len(read_obj.pages)
print(pageno)

# print(dir(read_obj)) 
file2=open("file.txt","w",encoding='utf-8')


for i in range(pageno):
    page=read_obj.pages[i]
    text=page.extract_text()
    print(text)
    file2.write(text)
    print()


file2.close()
#Close the pdf file

pdf_file.close()

