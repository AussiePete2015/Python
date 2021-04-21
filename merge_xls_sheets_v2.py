import openpyxl
import sys
import pandas as pd
import os, fnmatch

def find(pattern, path):
	try:

		# find the xlsx file in the folder and return the name including extension
		result = []
		for root, dirs, files in os.walk(path):
			for name in files:
				if fnmatch.fnmatch(name, pattern):
					result.append(os.path.join(root, name))

	except:
		print ("Oops!", sys.exc_info()[0], "occurred.")
		sys.exit(1)

	return result

def readxlsx(book, path):
	try:

		# Reading the xlsx file and setting it active
		print (book)
		print (path)
		xlsx_wb = openpyxl.load_workbook(path + book)
		xlsx_wb = xlsx_wb.active

		# read the xlsx data
		xlsx_data = xlsx_wb.values

		# reference the column names starting from the beginning
		xlsx_cols = next(xlsx_data)[0:]

		# load data into a dataframe with column names
		df = pd.DataFrame(xlsx_data, columns = xlsx_cols)

	except:
		print ("Oops!", sys.exc_info()[0], "occurred.")
		sys.exit(1)

	return df

def writexlsx(master_wbook, data1, data2):
	try:
		# create excel writer object
		writer = pd.ExcelWriter(master_wbook[0], engine='openpyxl')

		mwbook = openpyxl.load_workbook(master_wbook[0])
		writer.mwbook = mwbook

		# write dataframe to excel
		df1.to_excel(writer, sheet_name = 'Business1', index=False)
		df2.to_excel(writer, sheet_name = 'Business2', index=False)

		# save the excel
		writer.save()
		writer.close()
		print('DataFrame is written successfully to Excel File.')

	except:
		print ("Oops!", sys.exc_info()[0], "occurred.")
		sys.exit(1)

	return

if __name__ == '__main__':
	# variables used in program
	xlsx_data_path = '/Users/s59769/Downloads/test/'
	xlsx_path = xlsx_data_path + 'data/'
	xlsx_master = 'master.xlsx'
	xlsx_books = ['Book1.xlsx', 'Book2.xlsx']

	xlsxfile = find(xlsx_books[0], xlsx_data_path)
	print (xlsxfile)

	master_xlsxfile = find(xlsx_master, xlsx_path)
	print (master_xlsxfile)

	df1 = readxlsx(xlsx_books[0], xlsx_data_path)
	print (df1)

	df2 = readxlsx(xlsx_books[1], xlsx_data_path)
	print (df2)

	writexlsx(master_xlsxfile, df1, df2)
