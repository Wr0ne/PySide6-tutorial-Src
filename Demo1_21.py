import os   #Demo1_21.py
main = 'student_main.py'   #主程序py文件
path = 'D:\\Python\\installer'   #主程序py文件所在路径
os.chdir(path)  #将主程序文件所在路径设置成当前路径
cmdTemplate = "pyinstaller -D {}".format(main)  #命令模板
os.system(cmdTemplate)  #执行编译命令
