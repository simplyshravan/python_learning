def pyramid(i):
   for j in range(i):
            for z in range(i-j):
                    print(' ',end='')
            for k in range(j+1):
                    print('* ',end='')
            print('')
   for j in range(1,i):
            for k in range(j+1):
                    print(' ',end='')
            for z in range(i-j):
                    print('* ',end='')
            print('')

inp=eval(input("enter the height of pyramid:"));
pyramid(inp);
