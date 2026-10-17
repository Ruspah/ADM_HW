#SUPERDIGIT
import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    res_string = n*k
    if len(res_string) == 1:
        output = int(res_string)
        return output   
    else:
        somma = 0
        for i in res_string:
            add = int(i)   
            somma += add
        iteration = str(somma)
        return superDigit(iteration, 1)
    
        
         
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

#BIRTHDAYCAKE
import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    m = max(candles)
    count = 0
    for i in range(len(candles)):
        if candles[i] == m:
            count += 1
    return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

#RUNNERUP
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    lista = list(arr)
    a = max(lista)
    nl = [x for x in lista if x!=a ]
    print(max(nl))
   
#LISTCOMPREHENSIONS
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    Perm = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]
    Output = [x for x in Perm if sum(x) != n]
    print(Output)

#PRINFUNCTION
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        a = i+1
        print (a, end = "")

#FUNCTION
def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else: leap = False
        else: leap = True
            
    # Write your logic here
    
    return leap

year = int(input())

#LOOPS
if __name__ == '__main__':
    n = int(input())
    i = 0
    while i < n :
        print(i**2)
        i += 1

#DIVISION
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = a // b
    d = a / b
    print(c)
    print(d)

#ARITHMETIC OPERATORS
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = a // b
    d = a / b
    print(c)
    print(d)

#IFELSE
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if n < 1 or n > 100:
    raise Exception("Out of constraint")
if n % 2 == 1 : 
    print("Weird")
else :
    if (n >= 2 and n <= 5) or n > 20 :
        print("Not Weird")
    else:
        print("Weird")
    
