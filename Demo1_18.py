from PySide6.QtCore import QObject , Signal  #Demo1_18.py

class signalDefinition(QObject):
    s1 = Signal()  #创建无参数的信号
    s2 = Signal(int)  #创建带整数的信号
    s3 = Signal(float)  #创建带浮点数的信号
    s4 = Signal(str)  #创建带字符串的信号
    s5 = Signal(int,float,str)  #创建带整数、浮点数和字符串的信号
    s6 = Signal(list)  #创建带列表的信号
    s7 = Signal(dict)  #创建带字典的信号
    s8 = Signal([int],[str])  #创建重载型信号，相当于创建了两个信号
    s9 = Signal([int,str],[str],[list])   #创建重载型信号，相当于创建了3个信号
    s10 = Signal([],[bool])  #创建重载型信号，一个不带参数，另一个带布尔型参数

    def __init__(self,parent=None):
        super().__init__(parent)
        self.s1.connect(self.slot1)  #信号与槽的连接
        self.s2.connect(self.slot2)
        self.s3.connect(self.slot3)
        self.s4.connect(self.slot4)
        self.s5.connect(self.slot5)
        self.s6.connect(self.slot6)
        self.s7.connect(self.slot7)
        self.s8[int].connect(self.slot8_1)
        #self.s8.connect(self.slot8_1)  #overload型信号的第1个信号可以不指定类型
        self.s8[str].connect(self.slot8_2)
        self.s9[int,str].connect(self.slot9_1)
        #self.s9.connect(self.slot9_1)  #overload型信号的第1个信号可以不指定类型
        self.s9[str].connect(self.slot9_2)
        self.s9[list].connect(self.slot9_3)
        self.s10.connect(self.slot10_1)
        self.s10[bool].connect(self.slot10_2)

        self.s1.emit()
        self.s2.emit(10)
        self.s3.emit(11.11)
        self.s4.emit('北京诺思多维科技有限公司')
        self.s5.emit(100,23.5,"北京诺思多维科技有限公司")
        self.s6.emit([1,8,'hello'])
        self.s7.emit({1:'Noise',2:'DoWell'})
        self.s8[int].emit(200)
        #self.s8.emit(200)  #overload型信号的第1个信号可以不指定类型
        self.s8[str].emit('Noise DoWell Tech.')
        self.s9[int,str].emit(300,"Noise DoWell Tech.")
        #self.s9.emit(300, "Noise DoWell Tech.") #overload型信号的第1个信号可不指定类型
        self.s9[str].emit('s9')
        self.s9[list].emit(["s9",'overload'])
        self.s10.emit()
        self.s10[bool].emit(True)
    def slot1(self):
        print("s1 emit")
    def slot2(self,value):
        print("s2 emit int:",value)
    def slot3(self,value):
        print("s3 emit float:",value)
    def slot4(self,string):
        print("s4 emit string:",string)
    def slot5(self,value1,value2,string):
        print("s5 emit many values:",value1,value2,string)
    def slot6(self,list_value):
        print("s6 emit list:",list_value)
    def slot7(self,dict_value):
        print("s7 emit dict:",dict_value)
    def slot8_1(self,value):
        print("s8 emit int:",value)
    def slot8_2(self,string):
        print("s8 emit string:",string)
    def slot9_1(self,value,string):
        print("s9 emit int and string:",value,string)
    def slot9_2(self,string):
        print("s9 emit string:",string)
    def slot9_3(self, list_value):
        print("s9 emit list:", list_value)
    def slot10_1(self):
        print("s10 emit")
    def slot10_2(self,value):
        print("s10 emit bool:",value)
if __name__ == '__main__':
    signalTest = signalDefinition()
#运行结果如下：
#s1 emit
#s2 emit int: 10
#s3 emit float: 11.11
#s4 emit string: 北京诺思多维科技有限公司
#s5 emit many values: 100 23.5 北京诺思多维科技有限公司
#s6 emit list: [1, 8, 'hello']
#s7 emit dict: {1: 'Noise', 2: 'DoWell'}
#s8 emit int: 200
#s8 emit string: Noise DoWell Tech.
#s9 emit int and string: 300 Noise DoWell Tech.
#s9 emit string: s9
#s9 emit list: ['s9', 'overload']
#s10 emit
#s10 emit bool: True
