# GCD
'''def gcd(a, b):
    if a == b:
        return a
    elif a < b:
        return gcd(b, a)
    else:
        return gcd(b, a - b)


a = 54
b = 12
print(gcd(a, b))'''


# o find the sum of digits of a positive integer recursively

'''def sum_digit(n):
    if n == 0:
        return 0
    return (n % 10 + sum_digit(n // 10))


#num = int(input("Enter the number:"))
num = 12345
result = sum_digit(num)
print("Sum of digits of number is: ", result)


'''
# the power of a number


'''def power(n,p):

	if p == 0:
		return 1
	return (n*power(n, p-1))

n= int(input('enter any number :'))
p=int(input('enter exponent number :'))
print(power(n,p))'''

# polindrome :

'''
def is_palindrome(n):
    if len(n) < 1:
        return True
    else:
        if n[0] == n[-1]:
            return is_palindrome(n[1:-1])
        else:
            return False
a=str(input("Enter string:"))
if(is_palindrome(a)==True):
    print("String is a palindrome!")
else:
    print("String isn't a palindrome!")

'''

# to perform binary search recursively on a sorted list
'''
def binary_srch(arr, low, high, element):
	if high >= low:
		mid = (high + low) // 2
		if arr[mid] == element:
			return mid
		elif arr[mid] > element:
			return binary_srch(arr, low, mid - 1, element)
		else:
			return binary_srch(arr, mid + 1, high, element)
	else:
		return -1
arr = [ 1, 3, 7, 10, 62 ]
element = 0
result = binary_srch(arr, 0, len(arr)-1, element)
if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in the array")

'''

#n to count the occurrences of a specific element in a list recursively.

def count_len(my_list, element):
    return my_list.count(element)

my_list = [1, 2, 3, 4, 2, 2, 5, 2, 6]
element = 2
print('{} has occurred {} times'.format(element,count_len(my_list, element)))