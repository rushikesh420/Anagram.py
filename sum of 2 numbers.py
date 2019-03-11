#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

def sum_of_num(a,k,n):
    for i in range(int(n)):
        comp = int(k) - int(a[i])
        if comp in a:
            print("Solution Found: {} and {}".format(a[i], comp))
            break
    else:
        print("No solutions exist")
        
a = []
n = input('Enter number of element in array: ')
print ('Enter numbers in array: ')
for i in range(int(n)):
    r = input()
    a. append(int(r))
print (a)
k = input('Enter sum of numbers: ')
sum_of_num(a,k,n)
