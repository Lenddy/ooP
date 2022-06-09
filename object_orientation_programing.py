
'''
objects and isnstances are the same
'class is = to the objet or the out line or the blueprint
clases can be anythin 

attributes are = what can the objet have  what abilityes can the objet poses 
attributes are variables inside of a class

Methods are = what can the objet do  what skills can the objet use
Methosd are funtions inside of a class


you can make the attributes and methods to be either private or public but they are public by default

pritvate methods or atributes dont get inhereted 
if you want that to happen you would have to use the key word protected


if you want the objet to have an atribute  by  defult  you can use a key work  = .constructor 

by using inheretance or in inheret the objet can have the same atributes as the privius objet and you can add mor stuf to that objetc
thik of it like a parent chield thing  if the parent have black hair the chilld will also have black hair but you can spefify aditionnal things

'''

from typing_extensions import Self


class Student:
    # costructor - constructing objects
    def __init__(self,first_name,last_name,insturctor,curent_stack):
        #Attributes - attributes are accesible in the entire class
        self.first_name = first_name
        self.last_name = last_name
        self.insturctor = insturctor
        self.curent_stack = curent_stack
        # methods
    def print_student_info(self):
        print("name:",self.first_name)
        print("last name:",self.last_name)
        print("the instructor:",self.insturctor)
        print("curent stack:",self.curent_stack)

Lenddy = Student("Lenddy","Morales","Alfredo","python")
Lenddy.print_student_info()

ana = Student("ana","estevez","nicol","wed fundamentals")
ana.print_student_info()


class User:
    def __init__(self,name,last_name,age,):
        self.name = name
        self.last_name = last_name
        self.age = age
    def user_info(self):
        print("name",self.name)
        print("last name",self.last_name)
        print("age",self.age)
user = User("Lenddy","Morales",18)
user.user_info()

class Grade:
    def __init__(self,topic,grade_mark):
        self.topic = topic
        self.grade_mark = grade_mark
    def grade_info(self):
        print("topic:",self.topic)
        print("grade mark:",self.grade_mark)
l = Grade("python",50)
l.grade_info()












class Id:
    def __init__(self,first_name,last_name,instructor,stack):
        self.first_name = first_name
        self.last_name = last_name
        self.instructor = instructor
        self.stack = stack
    def user(self):
        print("first name", self.first_name)
        print("last name ", self.last_name)
        print("isntructor",self.instructor)
        print("stack", self.stack)

Lenddy1 = Id("Lenddy","Morales","alfredo","python")
Lenddy1.user()
