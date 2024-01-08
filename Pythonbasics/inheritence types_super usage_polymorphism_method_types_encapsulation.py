# Types of methods/variable in a class - methods(instance,class, static) , class/instance variable

class laptop():
    # class variable - remains common for all objects of this class-so created outside
    # value doesnt change for every object - can be called by class name or object

    chargertype = "C TYPE"

    # constructor(a special type of instance method)- called when an instance is created by default -
    # store variables/fns whose values would change based on object

    def __init__(self):
        self.brand = ""  # instance variable - value may change based on each object-but initially set to ""
        self.price = 34

    # instance methods are specific to object instances and hence require self as a parameter which will automatically be passed when called
    # can only be called with object name not class

    def setprice(self, price):
        self.price = price

    def getprice(self):
        print(self.price)

    # method that is not specific to object but the class owns by itself.The parameter here will
    # automatically take the class name when called,if we use the keyword @classmethod before method definition.
    # if not, explicitly call the method by passing the class name as an argument
    # can be called by class name or any object name - changes the value set to all the objects

    @classmethod
    def changechargertype(cls):
        cls.chargertype = "B TYPE"
        print("type changed to B")

    # static method used when a function doesnt need the class or instance variable/fns to operate
    # can be called with class name or object name

    @staticmethod
    def info():
        print("This is a laptop class")


print(laptop.chargertype)
hp = laptop()
dell = laptop()
print(hp.chargertype)
hp.setprice(300)
hp.getprice()
laptop.changechargertype()  # now all objects value will also become b type
hp.changechargertype()  # now also, all objects value will also become b type

laptop.info()
hp.info()


# Inhertence - single,multiple,multi level, hierarchichal, hybrid(combo of previous types)

# single inheritence - kid inherits book class fns and variables
class Book():
    def fiction(self):
        print("Fiction book")


class Kid(Book):
    def chocolate(self):
        print("Chocolate")


k1 = Kid()
k1.fiction()
k1.chocolate()


# Multiple inheritence - daughter inherits both mom and book class variables/fns

class Mom():
    def watch(self):
        print("Mom's watch")


class Daughter(Mom, Book):
    def tab(self):
        print("Daughter's tab")


d1 = Daughter()
d1.tab()
d1.watch()
d1.fiction()


# Multilevel inheritence - dad inherits grandpa and son1 inherits both dad and grandpa though not explicitly given in son's fn
class Grandpa():
    def stories(self):
        print("Grandpa's stories")


class Dad(Grandpa):
    def phone(self):
        print("Dad's phone")


class Son1(Dad):
    def laptop(self):
        print("Son1's laptop")


s1 = Son1()
s1.laptop()
s1.phone()
s1.stories()
dadd = Dad()
dadd.stories()


# Hierarchical inheritance - Dad class being inherited by 3 diff classes(son1,2,3)

class Son2(Dad):
    pass


class Son3(Dad):
    pass


s2 = Son2()
s2.phone()
s2.stories()
s3 = Son3()
s3.phone()
s3.stories()


# Hybrid inheritence-more than 1 type (multi level and multiple)

class Son4(Dad, Book):
    pass


s4 = Son4()
s4.fiction()
s4.stories()
s4.phone()


# Polymorphism - a function override, single function used in multiple ways
# (no.of arguments and data types may vary)
# Example 1:
class Animal():
    def sound(self):
        print("Animal makes sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


d1 = Dog()
d1.sound()  # prints Dog barks as parent method is overriden by child


# Example 2:
def add(a, b, c=0):
    print(a + b + c)


# same fn can be used to add the elements by passing 2 or 3 arguments
add(10, 20)  # takes c=0 as per fn def as it is not given in the arguments
add(1, 2, 3)


# Super keyword usage

class A():
    def __init__(self):
        print("A initiated")

    def display(self):
        print("we are in class A")


class B(A):  # when object created, calls init fn of parent as there is no init fn for this class
    def display(self):
        print("we are in class B")


class C(A):
    def __init__(self):  # when object created, the parent init fn is not called as it is overridden
        print("C initiated")


class D(A):
    def __init__(self):
        super().__init__()  # when object created, the parent init fn is also called
        print("D initiated")


b = B()
c = C()
d = D()


# Run and see - different behaviour for multiple inheritence

class X():
    def __init__(self):
        print("X initiated")


class Y():
    def __init__(self):
        print("Y initiated")


class Z(Y, X):
    def __init__(self):
        super().__init__()  # calls the init of leftmost parent alone(Y)
        print("Z initiated")


z = Z()


class X1():
    def __init__(self):
        super().__init__()
        print("X1 initiated")


class X2(X1, X):
    def __init__(self):
        # calls the init of leftmost parent alone(X1)
        # but X1 also has a super line which makes it call X class which is the next parent of X2 although X and X1 are not related
        super().__init__()
        print("X2 initiated")


x = X2()

#Encapsulation
class Company():
    def __init__(self):
        self.country = "USA"            #Public variable - accessible outside class
        self._state = "Illinois"        #Protected variable - accessible only within this class and its child classes and objects
        self.__companyname = "Google"   #Private variable - Accessible only within this class..not even its objects outside class

    def company_name(self):
        print(self.__companyname)       #can access inside class

class Company1(Company):

    def display(self):
         print(self._state)
        # print(self.__companyname) #Error cant be accesesed outside its own class

c=Company()
print(c.country,c._state)
# print(c.__companyname) - Error as it is private
c.company_name() # can be used to access the private variable thru a fn inside class
c1=Company1()
print(c1._state)
c1.display()