#1 导入特定的函数
from pizza import make_pizza
make_pizza(16, "pepperoni")
make_pizza(12, "mushroom", "green peppers", "extra cheese")

#2 使用as给函数指定别名
from pizza import make_pizza as mp
mp(16, "pepperoni")
mp(12, "mushroom", "green peppers", "extra cheese")

#3 使用as给模块指定别名
import pizza as p
p.make_pizza(16, "pepperoni")
p.make_pizza(12, "mushroom", "green peppers", "extra cheese")

#4 导入模块中的所有函数
from pizza import *
make_pizza(16, "pepperoni")
make_pizza(12, "mushroom", "green peppers", "extra cheese")
