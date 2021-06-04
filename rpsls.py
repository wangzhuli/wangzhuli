"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：王主俐
日期：2021年6月4日
"""

import random



def name_to_number(name):
    if name=="石头":
        name=0
    elif name=="史波克":
        name=1
    elif name=="布":
        name=2
    elif name=="蜥蜴":
        name=3
    elif name=="剪刀":
        name=4
    return name

def number_to_name(number):
    a=["石头","史波克","布","蜥蜴","剪刀"]
    return a[number]


name=input("请输入您的选择（石头、史波克、纸、蜥蜴、剪刀）：")
print("--------")
print("您的选择为：",name)


a1=name_to_number(name)

number=random.choice([0,1,2,3,4])
compute=number_to_name(number)
print("计算机的选择为：",compute)


a2=number

win=0
equl=0

if a1==a2:
    equl=1
   

if(a1==0 and a2==3)or(a1==0 and a2==4)or(a1==1 and a2==0)or(a1==2 and a2==0)or(a1==2 and a2==1)or(a1==3 and a2==2)or(a1==4 and a2==3)or(a1==4 and a2==2):
    win=1
else:
    win=0

if win==1 and equl==0:
    print("您赢了")
   
elif equl==0:
    print("计算机赢了")
   
else:
    print("您和计算机出的一样呢")
