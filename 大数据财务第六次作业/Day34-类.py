#1 创建和使用类
#1.1 创建Dog类
class Dog():
    '''一次模拟小狗的简单尝试'''
    def ___init___(self, name, age):
        '''初始化属性name和age'''
        self.name = name
        self.age = age
    def sit(self):
        '''模拟小狗被命令时蹲下'''
        print(self.name.title() + ' is now sitting.')
    def roll_over(self):
        '''模拟小狗被命令时打滚'''
        print(self.name.title() + " rolled over!")