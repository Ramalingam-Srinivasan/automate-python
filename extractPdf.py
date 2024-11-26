import camelot

#below code will read the pdf and extract it into csv format
table= camelot.read_pdf('requirement/sample_table.pdf',pages='1')
print(table)
table.export('foo.csv',f='csv',compress=True)
table[0].to_csv('foo.csv')