#def pyramid(i):
#   for j in range(i):
#            for z in range(i-j):
#                    print(' ',end='')
#            for k in range(j+1):
#                    print('* ',end='')
#            print('')

#inp=eval(input("enter the height of pyramid:"));
#pyramid(inp);
inp=int(input())
for i in range(inp):
    print(' '*(inp-1-i)+'* '*(i+1));
