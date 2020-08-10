# grxx = {}
# name = input("请输入你的姓名：")
#
# age = input("请输入你的年龄：")
#
#
#
# grxx['name'] = name
# grxx['age'] = age
#
# print(grxx)
#


class Dog():


    def __init__(self, name, age):

        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title()+' '+'is now sitting.')

    def roll_over(self):
        print(self.name.title()+' '+'rolled over')

# my_dog = Dog()

Dog('zhang san',8).sit()

Dog('zhang si',8).roll_over()


class Huang_dog(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)

Huang_dog('sss s',34).sit()