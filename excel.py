
# $ pip install xlrd

import xlrd

def getExcelData(xlsxPath, keys):
	xlsx = xlrd.open_workbook(xlsxPath)

	table = xlsx.sheets()[0]

	rowNum = table.nrows
	colsNum = table.ncols
	
	rows = []
	
	for i in range(1, rowNum):
		#获取每一行的数据
		row = table.row_values(i)
		
		#把每一行的数据配合上面的key打成对象
		rowObject = dict(zip(keys, row))
		
		rows.append(rowObject)
		
	return rows

# test
def plus(a,b):
	return a+b

result = plus(1,2)
print(result)