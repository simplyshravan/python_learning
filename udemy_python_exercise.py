##1
print(7**4)

##2
s="hi there is sam!"
newlist=s.split(" ")
print(newlist)

print(len(s.split(" ")))

###3
planet = "Earth"
diameter = 12742
print("The diameter of {} is {} kilometers.".format(planet,diameter))

###4
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2][0])

###5
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d.get('k1')[3].get('tricky')[3].get('target')[3])
print(d['k1'][3]['tricky'][3]['target'][3])

##6
def f(x):
    print(x.split("@")[-1])

f("my@domain.com")
###6
g = lambda xy : xy.split("@")[1]
print(g("my@domain.com"))


##7
def finddog(s):
    return 'dog' in s.lower().split()
    #for i in range(len(s.split(" "))):
    #     if s.split(" ")[i]=="dog":
    #         print("True")

finddog('Is there a dog here?')
###8
def countdog(z):
    count = 0
    for word in z.lower().split():
        if word == 'dog':
            count += 1
    print(count)
    j=0
    for i in range(len(z.split(" "))):
         if z.split(" ")[i]=="dog":
             j=j+1
    if j>0:
        print('found it {} time'.format(j))

countdog('is there dog a dog here')
####9
  
seq = ['soup','dog','salad','cat','great']
res=list(filter(lambda x:x[0]=='s' ,seq))
print(res)


###10
def caught_speeding(speed, is_birthday):
    if(is_birthday):
        birth=5
    else:
        birth=0
    if(speed <= 60 + birth):
        print('No ticket')
    elif (speed <= (80 + birth)):
        print('Small Ticket')
    else:# (speed=< 81+birth):
        print('Big TIcket')

caught_speeding(60,True)        
caught_speeding(65,True)
caught_speeding(65,False)
caught_speeding(66,False)
caught_speeding(66,True)
caught_speeding(81,False)
caught_speeding(81,True)
caught_speeding(85,False)
caught_speeding(85,True)


