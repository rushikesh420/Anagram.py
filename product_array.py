#Given an array of integers, return a new array such that each element at index i of the new array 
#is the product of all the numbers in the original array except the one at i.

def new_array(a,n):
    p = 1
    for i in range(int(n)):
        p = p * a[i]
    for i in range(int(n)):
        b.append(int(p / a[i]))
    print(b)

a = []
b = []
n = input('Enter number of element in array: ')
print ('Enter numbers in array: ')
for i in range(int(n)):
    r = input()
    a. append(int(r))
print (a)
new_array(a,n)