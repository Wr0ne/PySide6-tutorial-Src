from openpyxl import load_workbook   #Demo5_3.py
wbook = load_workbook("d:\\student.xlsx")

wsheet1 = wbook['学生成绩']
wsheet2 = wbook.get_sheet_by_name('Sheet')
print(wsheet1.title,wsheet2.title)  
for sheet in wbook:  #遍历工作表格
    print(sheet.title)
a = wbook.index(wsheet1)  #获取工作表格实例的序列号
b = wbook.get_index(wsheet2)  #获取工作表格实例的序列号
print(a,b)
