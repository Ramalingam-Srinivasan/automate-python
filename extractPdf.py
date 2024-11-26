import camelot

# Read the PDF file and extract the table from the first page
table = camelot.read_pdf('requirement/sample_table.pdf', pages='1')

# Print the extracted table information
print(table)

# Export the extracted table to a compressed CSV file
table.export('foo.csv', f='csv', compress=True)

# Save the first extracted table directly to a CSV file
table[0].to_csv('foo.csv')
