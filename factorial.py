#Write a recursive function to calculate the factorial of a number
#edit from jotham.
#edit from jotham.
def factorial(num):
    if num == 0:
        return 1
    return num* factorial(num-1)


print('Enter the number')
y = int(input())

result = factorial(y)
print(result)