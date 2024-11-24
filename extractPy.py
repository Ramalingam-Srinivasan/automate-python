import camelot

#below code will read the pdf and extract it into csv format
table= camelot.read_pdf('sample.pdf',pages='1')
print(table)
table.extract('foo.csv',f='csv',compress=True)
table[0].to_csv('foo.csv')