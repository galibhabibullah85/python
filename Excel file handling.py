"""---Must install pyexcel and pyexcel-xls by pip---"""
import pyexcel as pe

"""-------------Inserting records into the file---------"""
# data = [{
# 		'E-mail':'ahmostofa089@gmail.com'
# 	},
# 	{
# 		'E-mail':'ahmostofa089@gmail.com'
# 	}]

# p.save_as(records=data , dest_file_name='leads.xls')



# """-----------------Reading file------------------------"""
# # file = p.get_records(file_name='leads.xls') #list data-typed.Iterating with loop but not_recommended
# # file2 = p.iget_records(file_name='leads.xls') #generator data-typed.Iteratable with loop
# # for record in file:
# # 	print(record['E-mail'] , end='\n')



# #-----------Consoling records as a table-----------
# sheet_view = p.get_sheet(file_name='leads.xls')

# #--------------------Rows manupulation------------------
# # sheet_view.row += ['galibhabibullah785@gmail.com'] #appending row with records
# # sheet_view.row[2] = ['ahmostofa786@gmail.com'] #updating an exsisting row with records


# #--------------------Columns manupulation----------------
# # sheet_view.column += ['Status'] #appending column with records
# sheet_view.column += ['Status', 'safe', 'unsafe'] #appending column with records(recommended)
# sheet_view.column[1] = ['Status','safe','unsafe']
# sheet_view.save_as('leads.xls')
# print(p.get_sheet(file_name='leads.xls'))

# status = ['Status', 'safe', 'unsafe']
# file = pe.get_sheet(file_name='leads.xls')
# file.column[3] = status
# print(file)