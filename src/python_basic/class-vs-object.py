#coding:UTF-8

## __init__ create a instance
## use 'self' to refer or point to that instance
## use method to access value in a specific instance.
#####################################################
import math
class Point(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.radius = math.sqrt(self.x*self.x + self.y*self.y)
        self.angle = math.atan2(self.y,self.x)
    def cartesian(self):
        return (self.x, self.y)
    def polar(self):
        return (self.radius, self.angle)
    def distance(self, other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __cmp__(self, other):
        return self.x < other.x and self.y < other.y

class Segment:
        def __init__(self, start, end):
            self.start = start
            self.end = end
        def length(self):
            return math.sqrt(((self.start.x - self.end.x) *
                              (self.start.x - self.end.x))
                             + ((self.start.y - self.end.y) *
                                (self.start.y - self.end.y)))



cp1 = Point(1.0,2.0)
print(cp1.x)
cp2 = Point(4,6)
print(cp1.distance(cp2))
# print(Point.distance(cp1,cp2))
# print cp1
# # print cp1.__str__()
# print cp1.angle
print(cp1.radius)
# print cp1.cartesian()
print(cp1.polar())

x= cp1.polar()
#
# # print dir(cp1)
# # print dir(1)
# print dir("a string")
#
# ## don't do this way, python is bad at data hiding
# ## data hiding:one can only access instance status through method.
# ## change instance status directly, method will not recalculate.
# ## it will cause data not consistent
cp1.radius = 5.0
print (x)
# print cp1.radius
# print cp1.cartesian()

# p1 = Point(3.0, 4.0)
# p2 = Point(6.0, 8.0)
# print p1.__cmp__(p2)
# s1 = Segment(p1, p2)
# print s1.length()




# class inherit - extend to reuse
class Animal(object):

    def __init__(self):
        print('I am constructed. optional, used to set up and initialize variables')

    def run(self):
        print ('Animal is running...')

    def __del__(self):
        print('I am destructed. optional, and seldom used.')

class Dog(Animal):
    def run(self):
        print ('Dog is running...')

    def eat(self):
        print ('Eating meat...')

class Cat(Animal):
    pass

# testing code
dog = Dog()
dog.run()

# dog = 2 # reassign, cause hte destruction.

cat = Cat()
cat.run()
print(isinstance(cat,Animal))
#end testing code


# Python don't support abstract method(java,C#) or pure virtual function(C++).
# but there is replacement implementation to do thing like that
class Sheep(object):
  def get_size(self):
    raise NotImplementedError

class ChildSheep(Sheep):
    def get_weight(self):
        return 10
    # def get_size(self):
    #     return 15

childSheep = ChildSheep()
print(childSheep.get_weight())
# print(childSheep.get_size())  #will throw exception, if child not implement/override the get_size() method.

# class property (like static property in C#) can be shared between object of the class
class C:
    x= 100
    
    def myActionMethod(self):
        self.x = self.x + 1
        return self.x

print(C.x)
C.x=C.x+1
print(C.x)
obj = C() # Construct an object ans story it in a var.
print(C.myActionMethod(obj))
print(obj.myActionMethod())
print(C.x)



