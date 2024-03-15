'''1.Create a unittest for a module which has a class called Calculator. It has 5 methods add, sub,
mul, div and mod. All these methods must be tested with positive, negative float and integers including zero.'''

# import unittest
# import calc
# c=calc.calc
# class CalcTest(unittest.TestCase):
#     def test_add_int(self):
#         self.assertEqual(c.add(26,27), 53)
#         self.assertEqual(c.add(-26,27), 1)
#         self.assertEqual(c.add(-26,-27),-53)
#         self.assertEqual(c.add(26,-27),-1)
#         self.assertEqual(c.add(0,-27),-27)
#     def test_add_float(self):
#         self.assertEqual(c.add(26.4, 27.8), 54.2)
#         self.assertEqual(c.add(-26.6, 27.4), 0.8)
#         self.assertEqual(c.add(-26.3, -27.2),-53.5)
#         self.assertEqual(c.add(26.9, -27.2),-0.3)
#         self.assertEqual(c.add(0.0, -27.5),-27.5)
#
#     def test_sub_int(self):
#         self.assertEqual(c.sub(26,27),-1)
#         self.assertEqual(c.sub(-26,27),-53)
#         self.assertEqual(c.sub(-26,-27), 1)
#         self.assertEqual(c.sub(26,-27), 53)
#         self.assertEqual(c.sub(0,-27), 27)
#
#     def test_sub_float(self):
#         self.assertEqual(c.sub(26.4, 27.8),-1.4)
#         self.assertEqual(c.sub(-26.6, 27.4),-54)
#         self.assertEqual(c.sub(-26.4, -27.8), 1.4)
#         self.assertEqual(c.sub(26.6, -27.4), 54)
#         self.assertEqual(c.sub(0.0, -27.5),-27.5)
#
#     def test_mul_int(self):
#         self.assertEqual(c.mul(2,3),6)
#         self.assertEqual(c.mul(-2,3),-6)
#         self.assertEqual(c.mul(-2,-3), 6)
#         self.assertEqual(c.mul(2,-3), -6)
#         self.assertEqual(c.mul(0,-2), 0)
#
#     def test_mul_float(self):
#         self.assertEqual(c.mul(2.5,3.5),8.75)
#         self.assertEqual(c.mul(-2.5,3.5),-8.75)
#         self.assertEqual(c.mul(-2.5,-3.5), 8.75)
#         self.assertEqual(c.mul(2.5,-3.5), -8.75)
#         self.assertEqual(c.mul(0.5,-2.5), -1.25)
#
#     def test_div_int(self):
#         self.assertEqual(c.div(10,5), 2)
#         self.assertEqual(c.div(-10, 5), -2)
#         self.assertEqual(c.div(-10, -5), 2)
#         self.assertEqual(c.div(10, -5), -2)
#         self.assertEqual(c.div(0, -5), 0)
#         # self.assertEqual(c.div(4, 0), 0)
#
#     def test_div_float(self):
#         self.assertEqual(c.div(10.0,5.0), 2)
#         self.assertEqual(c.div(-10.0, 5.0), -2)
#         self.assertEqual(c.div(-10.0, -5.0), 2)
#         self.assertEqual(c.div(10.0, -5.0), -2)
#         self.assertEqual(c.div(0, -5.0), 0)
#         # self.assertEqual(c.div(4.3, 0), 0)
#
# if __name__ == '__main__':
#     unittest.main()


'''2.Create a student report in xlsx which will have 4 columns student, maths, science, english 3 subjects marks.
 Now create a line chart for this data in xlsx.'''

# import xlsxwriter
# workbook = xlsxwriter.Workbook('Sudent_report.xlsx')  # Creating a workbook
#
# worksheet = workbook.add_worksheet()
# chart = workbook.add_chart({'type': 'line'})
# header_format = workbook.add_format({'bold': True, 'align': 'center'})
# header_format2 = workbook.add_format({'align': 'center'})
# # # # #
# data_str = ['Harsha', 'Riya', 'Jeel', 'Ayushi']
# data1 = [60, 40, 50,]
# data2 = [80, 30, 60]
# data3 = [70, 20, 90]
# data4 = [40, 20, 90]
# # # # # # # #
# worksheet.write('A3','Subjects',header_format)
# worksheet.write('A5', 'Maths')
# worksheet.write('A6', 'Science')
# worksheet.write('A7', 'English')
# worksheet.write('C3',"Student's name",header_format)
# worksheet.write_row('B4',data_str,header_format2)
# # # # # # #
# worksheet.write_column('B5', data1,header_format2)
# worksheet.write_column('C5', data2,header_format2)
# worksheet.write_column('D5', data3,header_format2)
# worksheet.write_column('E5', data4,header_format2)
# # # # #
# chart.add_series({
#     'name': ['Sheet1',4,0],
#     'categories': ['Sheet1', 3, 1, 3, 4],
#     'values': ['Sheet1', 4, 1,4,4]
# })
# # # # # # #
# chart.add_series({
#     'name': ['Sheet1', 5, 0],
#     'values': ['Sheet1', 5, 1, 5, 4]
# })
# # # # # # #
# chart.add_series({
#     'name': ['Sheet1', 6, 0],
#     'values': ['Sheet1', 6, 1, 6, 4]
# })
# # # # # # #
# # # # # #
# chart.set_title({'name': 'Student Report'})
# # # # # #
# worksheet.insert_chart('B9', chart)
# # # # # #
# workbook.close()

'''3.Create a sales report in xlsx which will have the following data.
Sales Person 1 : 78,000.0
Sales Person 2 : 32,000.0
Sales Person 3 : 45,000.0
Sales Person 4 : 11,000.0
Sales Person 5 : 20,000.0
Create a Pie Chart with the above data.'''

# import xlsxwriter
# workbook = xlsxwriter.Workbook('Sales_report.xlsx')  # Creating a workbook
#
# worksheet = workbook.add_worksheet('Sales Report')
# chart = workbook.add_chart({'type': 'pie'})
#
#
# data_dict = {'Sales Person 1' : 78000.0,
#     'Sales Person 2': 32000.0,
#     'Sales Person 3': 45000.0,
#     'Sales Person 4': 11000.0,
#     'Sales Person 5': 20000.0
# }
# worksheet.write('A1', 'Employee')
# worksheet.write('B1', 'Score')
#
# row = 1
#
# for saleperson, score in data_dict.items():
#     worksheet.write(row, 0, saleperson)
#     worksheet.write(row, 1, score)
#     row += 1
#
#
# chart.add_series({
#     'name': 'Sales Report',
#     'categories': ['Sales Report', 1, 0, 5, 0],
#     'values': ['Sales Report', 1, 1,5,1]
# })
#
# chart.set_title({'name': 'Sales Report'})
#
# worksheet.insert_chart('B9', chart)
#
# workbook.close()

'''4. Create a medals report in xlsx for olympics based on countries as shown below.
Country, Gold, Silver, Bronze, Total
Country 1, 15, 20, 25, 60
Country 2, 8,15,10, 33
Country 3, 12,25,10, 47
Country 4, 21,12,13, 50
Country 5, 18,29,30, 77
Create a Column chart with 3 medals gold, silver and bronze data.
Create another Line chart with only total medals data.'''

# import xlsxwriter
# workbook = xlsxwriter.Workbook('Medal_report.xlsx')  # Creating a workbook
#
# worksheet = workbook.add_worksheet()
# header_format = workbook.add_format({'bold': True, 'align': 'center'})
# header_format2 = workbook.add_format({'align': 'center'})
# # # # #
# col_data=['Countries','Country 1','Country 2','Country 3','Country 4','Country 5']
# worksheet.write_column('A1',col_data)
# data_str = [['Gold', 'Silver', 'Bronze', 'Total'],
#             [15, 20, 25, 60],
#             [8,15,10, 33],
#             [12,25,10, 47],
#             [21,12,13, 50],
#             [18,29,30, 77]
#             ]
#
# row = 0
# for data in data_str:
#     worksheet.write_row(row,1,data)
#     row += 1
#
# chart = workbook.add_chart({'type': 'column'})
# chart2 = workbook.add_chart({'type': 'line'})
# #
# chart.add_series({
#     'name': ['Sheet1',0,1],
#     'categories': ['Sheet1', 1, 0, 5, 0],
#     'values': ['Sheet1', 1, 1,5,1]
# })
# # # # # # # #
# chart.add_series({
#     'name': ['Sheet1',0,2],
#     'values': ['Sheet1', 1, 2,5,2]
# })
# # # # # # # #
# chart.add_series({
#     'name': ['Sheet1',0,3],
#     'values': ['Sheet1', 1, 3,5,3]
# })
# chart2.add_series({
#     'name': ['Sheet1', 0, 4],
#     'categories': ['Sheet1', 1, 0, 5, 0],
#     'values': ['Sheet1', 1, 4, 5, 4]
#
# })
#
# chart.set_title({'name': 'Medal Report'})
# chart2.set_title({'name': 'Medal Report'})
#
# worksheet.insert_chart('A7', chart)
# worksheet.insert_chart('I9', chart2)
#
# workbook.close()


'''5. Read an Excel file and prepare a data as shown below.
Excel Data
Name SurName Gender Age City Nationality
Anup Chavda Male 36 Gandhinagar Indian
Yogesh Sakhreliya Male 36 Gandhinagar Indian
Sohil Patel Male 35 Vadodara Indian
Krutarth Buch Male 30 Vadodara Indian
Meet Dholakia Male 29 Vadodara Indian
Komal Patel Female 26 Ahmedabad Indian
Sneha Shah Female 28 Ahmedabad Indian
Himangi Sharma Female 24 Pune Indian
Priya Bhardwaj Female 25 Pune Indian
Akanksha Tyagi Female 26 Bangaluru Indian
Bhumi Trivedi Female 28 Bangaluru Indian


Result: You need to create a dictionary
{
‘Male’:[
{‘name’: ‘Anup Chavda’, ‘age’: 36, ‘city’:’Gandhinagar’, ‘nationality’:’Indian’},
{‘name’: ‘Yogesh Sakhreliya’, ‘age’: 36, ‘city’:’Gandhinagar’, ‘nationality’:’Indian’}
.......
]
‘Female’:[
{‘name’: ‘Komal Patel’, ‘age’: 26, ‘city’:’Ahmedabad’, ‘nationality’:’Indian’},
{‘name’: ‘Sneha Shah’, ‘age’: 28, ‘city’:’Ahmedabad’, ‘nationality’:’Indian’}
.......
]
}
'''

# import xlrd
#
#
# wb = xlrd.open_workbook('ex5.xlsx')
#
# # # Get All Sheets
# # sheets = wb.sheets()
# # print(sheets)
# # # #
# # for sheet in sheets:
# #     print(sheet.name)
#
# # Get Sheet Names
# sheet_names = wb.sheet_names()
# print(sheet_names)
#
# sheet = wb.sheet_by_index(0)
# print(sheet)
# # #
# print(sheet.name)
# print(sheet.nrows)
# print(sheet.ncols)
#
#
#



# import openpyxl
#
# df = openpyxl.load_workbook('ex5.xlsx')
# # print(df)
# #
# # print(dir(df))
# #
#
# # # Get All Sheets
# sheets = df.worksheets
# # print(sheets)
# # #
# # for sheet in sheets:
# #     # print(dir(sheet))
# #     print(sheet.title)
# #
# # # Get Sheet Names
# # sheet_names = df.sheetnames
# # print(sheet_names)
# # # #
# # # # # # Select Sheet by Name
# sheet_by_name = df['Sheet1']
# # print(sheet_by_name)
# sheet = sheet_by_name

# # # # # Iterating through all rows
# for rw in sheet.iter_rows(1,sheet.max_row):
#     print(rw)
#     for cell in rw:
#         print(cell.value)

# ls=[[ele.value for ele in ele_list]for ele_list in  sheet.iter_rows(2,sheet.max_row)]
#
#
# print(ls)
# dict_keys=['Male','Female']

# for i in range(0,10):
#     for j in range(0,4):
#        if 'Male' in ls:
# dictt={dict_keys[0]:ls[i][j] for i in range(0,10) for j in range(0,4)}

# =============================================================================
# import openpyxl
# workbook = openpyxl.load_workbook('ex5.xlsx')
# worksheet = workbook.active
#
#
#
# result = {}
# result_dict = {f'Male': [],
#            'Female': [],'Gender':[]}
#
# for value in worksheet.iter_rows(values_only=True):
#     print(value)
#
#
#
# for value in worksheet.iter_rows(min_row=1, values_only=True):
#     gender = value[2].strip()
#     emp_data = {
#         'Name':value[0] + ' '+ value[1],
#         'Age':value[3],
#         'City':value[4],
#         'Nationality':value[-1]
#
#     }
#     print(gender)
#     # result[emp_gen] = emp_data
#     result_dict[gender].append(emp_data)
#     print(emp_data)
#
#
# result_dict.popitem()
# print(result_dict)

'''6. Create a word document with header as Employee Experience Certificate, Write a
paragraph for his experience description.
Mention his projects as ordered list.
Mention his skills with unordered list.
Create a table with the following details
Total no of years Total Working Days Worked Days Leaves
4 1056 1016 40
Total Leaves Paid Leave Sick Leave Unpaid Leave
40 25 5 10'''

# from docx import Document
#
# document = Document()
#
# section = document.sections[0]
# header = section.header
# paragraph = header.paragraphs[0]
# paragraph.text = 'Employee Experience Certificate'
#
#
#
# p = document.add_paragraph('Digital Marketing Specialist')
# p.bold = True
# p = document.add_paragraph('''Pinnacle Climbing Gear
# H: 06/2015 - 09/2017 ® Madison, WI \n• Implemented first SEO-driven organic strategy which boosted site visits by 200% in 8 months while increasing
# total sales by 65%.
# • Led a 6 person team to write 10 articles a week and obtain an average of 8 quality backlinks per week.
# • Created an email marketing strategy which increased repeat buying from 20% to 35%.''')
#
# document.add_paragraph(
#     'first item in unordered list', style='List Bullet'
# )
# document.add_paragraph(
#     'second item in unordered list', style='List Bullet'
# )
# document.add_paragraph(
#     'third item in unordered list', style='List Bullet'
# )
# # # # #
# document.add_paragraph(
#     'first item in ordered list', style='List Number'
# )
# document.add_paragraph(
#     'second item in ordered list', style='List Number'
# )
# document.add_paragraph(
#     'third item in ordered list', style='List Number'
# )
# # # # #
# records = (
#     (4, 1056,1016,40),
#     ('Total Leaves','Paid Leave','Sick Leave','Unpaid Leave'),
#     (40,25,5,10)
# )
# # # # #
# table = document.add_table(rows=1, cols=4)
# # # # #
# print(table.rows)
# print(table.rows[0])
# hdr_cells = table.rows[0].cells
# print(hdr_cells)
# print(hdr_cells[0])
# # # #
# hdr_cells[0].text = 'Total no of years'
# hdr_cells[1].text = 'Total Working Days'
# hdr_cells[2].text = 'Worked Days'
# hdr_cells[3].text = 'Leaves'
#
# for year,tdays,tworkdays,leaves in records:
#     row_cells = table.add_row().cells
#     row_cells[0].text = str(year)
#     row_cells[1].text = str(tdays)
#     row_cells[2].text = str(tworkdays)
#     row_cells[3].text = str(leaves)
#
#
# document.save('Experience_letter.docx')

'''7. Read the data written in the above document file. For table data prepare a dictionary with their headers.'''

# from docx import Document
#
# # Opening Document
# document = Document('Experience_letter.docx')
# #
# # print(dir(document))
# #
# # Reading Sections
# print(document.sections)
# section = document.sections[0]
# print(section)
# # # Header and Footer
# print(section.header.paragraphs[0].text)
# print(section.footer.paragraphs[0].text)
# #
# # # Reading Paragraphs
# print(document.paragraphs)
# paras = [p.text for p in document.paragraphs]
# print(paras)
# # #
# # # Reading Table Data
# print(document.tables)
# for table in document.tables:
#     data = [[cell.text for cell in row.cells] for row in table.rows]
#     print(data)
#     # print(list(table))
# dict_data={i:j for (i,j) in zip(data[0],data[1])}
# dict_data2={i:j for (i,j) in zip(data[2],data[3])}
# dict_data.update(dict_data2)
# print(dict_data)

# # print(dir(document))

'''8. Create a CSV from the following list of dictionary. [
{‘name’:’Infosys’, ‘location’:’Pune’,’strength’:40,000.0}, 
{‘name’:’TCS’, ‘location’:’Gandhinagar’,’strength’:80,000.0}, 
{‘name’:’Wipro’, ‘location’:’Banguluru’,’strength’:65,000.0}, 
{‘name’:’Accenture’, ‘location’:’Gurugram’,’strength’:45,000.0}, 
{‘name’:’Capegemini’, ‘location’:’Mumbai’,’strength’:32,000.0},
]'''

# import csv
#
# headers = ['Name', 'Location','Strength']
#
# values = [
#     {'name':'Infosys','location':'Pune', 'strength':40000.0},
#     {'name':'TCS','location':'Gandhinagar','strength':80000.0},
#     {'name':'Wipro','location':'Banguluru', 'strength':65000.0},
#     {'name':'Accenture', 'location':'Gurugram','strength':45000.0},
#     {'name':'Capegemini', 'location':'Mumbai', 'strength':32000.0}
# ]
#
# f1 = open('Employee.csv', 'w')
#
# csv_writer = csv.writer(f1)
#
# csv_writer.writerow(headers)
#
# csv_writer.writerows(val.values() for val in values)
#
# f1.close()

'''9. Read a CSV file and create a list of dictionary as shown below.
CSV Data
ERP Establishment Users Cost
Odoo 2007 5000000 2000.00
Flectra 2019 5000 500.00
ERPNext 2015 12000 1200.00
Oracle Netsuite 2008 2500000 4500.00
MicrosftDynamics 2006 4500000 8500.00
SAP 2001 12000000 10000.00
List
[
(‘SAP’,20001, 12000000, 10000.00),
(‘Microsoft Dynamics’, 2006, 450000, 8500.00),
(‘Odoo’, 2007, 5000000, 2000.00).
........
]'''

# import csv
# f1 = open('erp.csv', 'r')
# csv_reader = csv.reader(f1)
# print(csv_reader)
# ls=[tuple(ele) for ele in csv_reader]
# print(ls)



#
# from openpyxl import Workbook
# wb = Workbook()
#
# # grab the active worksheet
# ws = wb.active
#
# # Data can be assigned directly to cells
# ws['A1'] = 42
#
# # Rows can also be appended
# ws.append([1, 2, 3])
#
# # Python types will automatically be converted
# import datetime
# ws['A2'] = datetime.datetime.now()
#
# # Save the file
# wb.save("sample.xlsx")




# a=list(map(int,(input("ENter three numbers: ").split())))
# print(a,type(a))
# print(min(a),max(a))