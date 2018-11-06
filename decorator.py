def myfunc(x ,y):
     print('inside myfunc')
     return x+y

def myfunc2(x,y,z):
    return myfunc(x,y)+z

#print(myfunc(4,5))
print(myfunc2(4,5,7))
print('###############################################')

#################################################################################################

def myfunc3(func,x,y,z):
    def inner():
        print('inside myfunc3 inner')
        return func(x,y)+z
    return inner

#print(myfunc3(myfunc,4,5,10))
print('###############################################')
call_func=myfunc3(myfunc,4,5,10)  #myfunc3 act as decorator here
call_func()

#################################################################################################
def myfunc31(func,x,y,z):
    def inner():
        print('inside myfunc31 inner')
        func(x,y)+z
    return inner

def myfunc32(func,x,y,z):
    def inner():
        print('inside myfunc32 inner')
        func(x,y)+z
    return inner

def myfunc33(x ,y):
     print('inside myfunc33')
     return x+y
#print(myfunc3(myfunc,4,5,10))
print('###############################################')
callfunc=myfunc31(myfunc33,4,5,10) #myfunc31 is decorator
callfunc()
callfunc=myfunc32(myfunc33,4,5,10) #myfunc32 is decorator
callfunc()
#################################################################################################

def myfunc5(func):
    def inner(x,y):
        print('inside myfunc5 inner')
        return func(x,y)
    return inner

@myfunc5
def decorate(x,y):
    print("calling decorate")
    return x+y



#print(myfunc5(decorate))
print('###############################################')
decorate(4,5) 

#################################################################################################

def myfunc6(func):
    def inner(x,y):
        print('inside myfunc6 inner')
        func(x,y)
        print('finishing myfunc6 inner')
    return inner

def myfunc7(func):
    def inner(x,y):
        print('inside myfunc7 inner')
        func(x,y)
        print('finishing myfunc7 inner')
    return inner


@myfunc6
@myfunc7
def decorate1(x,y):
    print("calling decorate1")



#print(myfunc5(decorate))
print('###############################################')
decorate1(14,15)


#################################################################################################


def myfunc8(func):
    def inner(x,y):
        print('inside myfunc8 inner')
        return func(x,y)
        print('finishing myfunc8 inner')
    return inner

def myfunc9(func):
    def inner(x,y):
        print('inside myfunc9 inner')
        return func(x,y)
        print('finishing myfunc9 inner')
    return inner


@myfunc6
@myfunc7
def decorate2(x,y):
    print("calling decorate2")
    return x+y



#print(myfunc5(decorate))
print('###############################################')
decorate2(14,15)





















