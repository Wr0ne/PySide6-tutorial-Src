import  os  #Demo1_20.py
qrc = 'image.qrc'   #被转换的ui文件
py = 'image_rc.py'   #转换后的py文件
path = 'd:\\python'   #ui文件所在路径
os.chdir(path)  #将ui文件所在路径设置成当前路径
cmdTemplate = "PySide6-rcc  {qrc}  -o  {py}".format(qrc=qrc, py=py)  #文本模板
os.system(cmdTemplate)  #执行编译命令
