import tabula
#Variable that store the path of the pdf
pdf_file = "demo.pdf"
#Variable that store the desired output file and its name
csv_file = "output.csv"
# Converting the PDF file to CSV using convert_into method
tabula.convert_into(pdf_file, csv_file, output_format="csv", pages="all")