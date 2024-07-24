from openpyxl import load_workbook  #Demo5_5.py
wbook = load_workbook("d:\\student.xlsx")
wsheet = wbook['学生成绩']
cell_range = wsheet["A2:F6"]  #单元格切片，返回值是按行排列的单元格元组
for i in cell_range:  # i是行单元格元组
    for j in i:  # j是单元格
        print(j.value,end=' ')  # 输出元组中单元格的值
    print()
columnA = wsheet['A']  # columnA是A列单元格元组
row1 = wsheet['1']  # row1是第1行单元格元组
row2 = wsheet[2]   # row2是第2行单元格元组
columnB_F = wsheet["B:F"]  # columnB_F是从B列到F列单元格元组
row1_2 = wsheet["1:2"]  # row1_2是第1行到第2行单元格元组
row3_5 = wsheet[3:5]    # row3_5是第3行到第5行单元格元组
for i in columnA:   # i是A列中的单元格
   print(i.value,end=' ')
print()
for i in columnB_F:  # i是列单元格元组
    for j in i:   # j是单元格
        print(j.value,end=' ')
    print()
for i in row3_5:  # i是行单元格元组
    for j in i:  # j是单元格
        print(j.value,end=' ')
    print()
for i in wsheet.values:  #输出工作表格中所有单元格的值
    for j in i:
        print(j,end=' ')
    print()
cell_range = wsheet[wsheet.dimensions] #获取工作表格中所有数据的单元格
for i in cell_range:   #输出工作表格中所有单元格的值
    for j in i:
        print(j.value,end=' ')
    print()
