def pyramid(i):
   for j in range(i):
            for z in range(i-j):
                    print(' ',end='')
            for k in range(j+1):
                    print('* ',end='')
            print('')

inp=eval(input("enter the height of pyramid:"));
#inp1=input();
pyramid(inp);
#print(List(inp1));

#for i in inp1:
#    print(i)

#while input()!='':
#    k=input()
#    print(k)

