import camelot
 

# extract all the tables in the PDF file
abc = camelot.read_pdf("BranchChange.pdf")   #address of file location
 
# print the first table as Pandas DataFrame
print(abc[0].df)