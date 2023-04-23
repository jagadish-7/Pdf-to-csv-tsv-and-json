import tabula
#Variable that store the path of the pdf
pdf_file = "demo.pdf"
#Variable that store the desired output file and its name
json_file = "output.json"
# Converting the PDF file to JSON
tabula.convert_into(pdf_file, json_file, output_format="json", pages="all")