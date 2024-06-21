
# def reverse(n):
#     rev = 0

#     while(n>0):
#         a = n%10
#         rev= rev *10 +a
#         n =n // 10
#     return rev

        

def reverse(number):
    rev = 0
    # Check if the number is negative
    negative_num = number < 0
    # Work with the absolute value of the number
    number = abs(number)
    
    while number > 0:
        a = number % 10
        rev = rev * 10 + a
        number = number // 10
    
    # If the number was negative, return the negative of the reversed number
    return -rev if negative_num else rev

# Prompt the user to enter a number
# print("Enter a number: ")
number = int(input("Enter a number: "))

print('Reversed:',reverse(number))
