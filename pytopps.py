# inheritance

# class parent():
#     def par(self):
#         print("something")
    
# class child(parent):
#     def chi(sefl):
#         print("hello world")
#         super().par()
# c = child()
# c.chi()


# class parent():
#     a,b = 10,20

# class child(parent):
#     x,y = 100,200
#     def add(self,i,j):
#         print(i+j)
#         print(self.x+self.y)
#         print(self.a+self.b)

# obj = child()
# obj.add(30,40)

# a,b = 1,2
# class parent():
#     a,b = 10,20
# class child(parent):
#     a,b = 100,200
#     def add(self,a,b):
#         print(a+b)
#         print(self.a+self.b)
#         print(super().a+super().b)

#         print(globals()["a"]+globals()["b"])

    
# c = child()
# c.add(1000,2000)


# class a():
#     n = 10
#     def __init__(self,name):
#         print("this is my first code",name)

# class b(a):
#     def hello(self):
#         super().__init__(self)
#         print(a.n)
       
# c = b("bhaskar")
# c.hello()

# types of inheritance
# single inheritance
# multi level inheritance
# multiple inheritance
# heirarachi inheritance
# hybrid inheritance



# class person:
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
# class emp(person):
#     def __init__(self,first,last,id):
#         super().__init__(first,last)
#         self.id = id
#     def __str__(self):
#         return "my name {} {}  and my id {}".format(self.first,self.last,self.id)
# c = emp("bhaskar","badivenkatagalla",123)
# print(c)



# class parent():
#     pass
# class child(parent):
#     pass
# c = child()         # reference variable or instance object
# p = parent()          # reference variable or instance object
# print(isinstance(c,parent))
# print(isinstance(p,parent))
# print(isinstance(c,object))



# polymorphism

# overloading
# over riding

# class parent:
#     def marr(self):
#         print("bad girl")
# class child(parent):
#     def marr(self):
#         print("good girl")
# c = child()
# c.marr()

# class parrot():
#     def fly(self):
#         print("parrot can fly")
#     def swim(self):
#         print("parrot can't swim")
# class pengwin():
#     def fly(self):
#         print("pengwin can't fly")
#     def swim(self):
#         print("pengwin can swim")


# # common interphase
# def flying_test(bird):
#     bird.fly()
#     bird.swim()
# p = parrot()
# pe = pengwin()

# flying_test(p)
# flying_test(pe)


# class bajaj():
#     def speed(self):
#         print("the speed of bajaj in good")
# class pulser():
#     def speed(self):
#         print("it was really awsome")
# # common interfaces
# def speed_test(company):
#     company.speed()

# # creating of objects
# b = bajaj()
# p = pulser()
# speed_test(p)


# encapsulation

# class myclass():
#     __a = "this is the private variable"
#     def __first(self):
#         print(self.__a)
#     def mainMethod(self):
#         print("calling of private method:-")
#         self.__first()
# c = myclass()
# c.mainMethod()

# class and object concept

# class myFirstclass():
#     def greeting(sefl):
#         print("hello world")

# Object = myFirstclass()
# Object.greeting()

# inheritance concept

# class baseClass():
#     def something(self,a,b):
#         print("sum of a and b is ",a+b)
# class derivedClass(baseClass):
#     pass
# obj = derivedClass()
# obj.something(12,13)

# # heirarchi inheritance
# class baseClass():
#     def something(self,a,b):
#         print("sum of a and b is ",a+b)
# class derivedClass1(baseClass):
#     pass

# class derivedClass2(baseClass):
#     pass

# class derivedClass3(baseClass):
#     pass
# obj = derivedClass3()
# obj.something(12,13)


# multiple inheritance

# class baseClass1():
#     def something1(self):
#         print("base class 1")

# class baseClass2():
#     def something2(self):
#         print("base class 2")
# class derivedClass(baseClass1,baseClass2):
#     pass
# obj = derivedClass()
# obj.something1()
# obj.something2()


# multi-level inheritance

# class grandParent():
#     def grandp(self):
#         print("grandparent")

# class parent(grandParent):
#     def parent(self):
#         print("parent")
# class child(parent):
#     def child(self):
#         print("child")
# obj = child()
# obj.parent()
# obj.grandp()
# obj.child()


# encapsulation

# wrapping up the data 

# class myclass():
#     def __dis(self):
#         print("private method")
#     def public(self):
#         print("public method")
#         self.__dis()

# # object creating

# obj = myclass()
# obj.public()


# abstraction
# abstract class
# abstract method and concrete method

# from abc import ABC ,abstractmethod
# class absdemo(ABC):
#     @abstractmethod
#     def demomethod(self):
#         None
# class concretclass(absdemo):
#     def demomethod(self):
#         print("this is how it will work")

# c = concretclass()
# c.demomethod()


# polymorphism
# class poly:
#     def first(self):
#         print("hello world")
# class morphism(poly):
#     def first(self):
#         print("hello python")  # over riding the same methon in classes
# c = morphism()
# c.first()

# constructor
# __init__

# class myclass():
#     def __init__(self):
#         print("hi i am the constructor __init__")
# c = myclass()

# conversion of local var to class variables

# class myclass():
#     def add(self,a,b):
#         print("sum is ",a+b)
#         self.a = a
#         self.b = b
#     def mul(self):
#         print("product is ",self.a*self.b)
# c = myclass()
# c.add(2,3)
# c.mul()

# class myclass():
#     var = int(input("enter something:-"))
#     def add(self,a):
#         print("my roll number is ",a)
#         self.a = a
#         self.mul(self.var)
#     def mul(self,b):
#         print("the product is ",self.a*b)
# c = myclass()
# c.add(2)


# class myclass:
#     name = "bhaskar"
#     def __init__(self,peru):
#         print(peru)
#         print(self.name)
# c = myclass("boss")


# __str__

# class myclass():
#     def __str__(self):
#         return "this is bhaskar"

# c = myclass()
# print(c)

# class myclass():
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#     def __str__(self):
#         return "this is {} and my id is {}".format(self.name,self.id)

# c = myclass("bhaskar",308)
# print(c)

# __del__

# class myclass():
#     def __del__(self):
#         print("this is the del method")
# c = myclass()
# del c

# super() function

# class myclass():
#     def some(self):
#         print("this is about super pre-defined function")
# class myclass2(myclass):
#     def some2(self):
#         print("i am going to print.....")
#         super().some()
# c = myclass2()
# c.some2()


# naming of variables in two classes is same
# a,b = 100,200
# class class1:
#     a,b = 1,2
# class class2(class1):
#     a,b = 10,20
#     def numbers(self,a,b):
#         print(a+b)
#         print(self.a+self.b)
#         print(super().a+super().b)
#         print(globals()['a']+globals()['b'])

# c = class2()
# c.numbers(1000,2000)

# class main():
#     __name = "bhaskar"
#     def this(self):
#         print("my name is ",self.__name)
# c = main()
# c.this()















































































































































































