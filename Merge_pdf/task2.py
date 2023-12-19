#Merging two or more pdfs
import PyPDF2 as p2

pdf_list=["Mentoring-patent.pdf",'909.pdf']

writer=p2.PdfWriter()

# Merging algorithm

for file in pdf_list:
    reader=p2.PdfReader(open(file,"rb"))
    for page in reader.pages:
        writer.add_page(page)




#save the merged pdf document

with open("merged_file.pdf","wb") as f:
    writer.write(f)
#close the pdf writer
writer.close()


