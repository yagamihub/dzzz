# class magazine():
#     def __init__(self,cost,quantity,name):
#         self.cost=cost
#         self.quantity=quantity
#         self.name=name
#     def give_me_money(self):
#         self.squa=self.cost*self.quantity
#         print(self.squa,' грн вам нужно заплатить за товар под названием',self.name)
#
# tria=magazine(5,5,'Bread')
# tria.give_me_money()
class Employee():
    def __init__(self,name,surname,position):
        self.name=name
        self.surname=surname
        self.position=position
    def check_it_out(self):
        print('Привет,я',self.name,self.surname,',я работаю на должности',self.position)

num1=Employee('John','Falsewich','менеджер')
num2=Employee('Juan','Potatowich','генеральный директор')
num3=Employee('Ivan,','Stealerwich','зам.председателя')
num1.check_it_out()
num2.check_it_out()
num3.check_it_out()