#MRO - Method Resolution Order
class A:
    num = 10
class B(A):
    pass
class C(A):
    num = 1
class D(B,C):
    pass

#MRO is a rule which python follows, when we run a method which one to run

print(D.num) #we get 1
#it goes from D-B-C-A

print(D.mro())

#it goes through all the inheritance and base object
#we might avoid mro 

#e.g 2

class X: pass
class Y: pass
class Z: pass
class A(X,Y): pass
class B(Y,Z): pass
class M(B,A,Z): pass
print(M.__mro__)
#check depth first course , it is a bit confusing where we use MRO, as it can be complicated
#this strcture must not be used while coding
#this is a method where python checks the heirarchy of inheritance when we call a method or attribute