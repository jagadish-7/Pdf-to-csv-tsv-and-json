import tabula
#Variable that store the path of the pdf
pdf_file = "demo.pdf"
#Variable that store the desired output file and its name
tsv_file = "output.tsv"
# Converting the PDF file to TSV
tabula.convert_into(pdf_file, tsv_file, output_format="tsv", pages="all")