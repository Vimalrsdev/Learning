import matplotlib as plt
import numpy as np


# a= np.arange(10)
# b=(a*0)
# print(b)
# b[5]=1
# print(b)

# a=np.arange(10,50)
# print(a)

# b=a[::-1]
# print(b)


# a =np.arange(0,9)
# b=a.reshape(3,3)

# print(b)

# a = np.random.rand(3,3,3)
# print(a)

# a = np.diag([1,2,3,4], k=-1)
# pri

# a=np.tile([1,2,3,4,5],5)
# print(a)

# a= np.random.random(10)
# a.sort()
# print(a)

# a = np.full((2,5),6)
# print(a)

# a= np.diag([1,1,1])

# b=a.reshape(1,3,3)
# print(b)

# a = np.array([[1,2,3],[4,5,6]])
# b=a.transpose()
# c=b.flatten()


# print(c)

# a = np.array([[1,2,3],[4,5,6]])
# b=a.flatten()
# print(b[5])

# a = np.arange(12)
# b= a.reshape(3,4)
# c = np.diag(b)
# print(c)

# a = np.linspace(3,10,50)
# print(a)


# a =np.arange(1,29)
# b=a.reshape(4,7)

# c =np.tile(b,(12,1,1))

# d =np.tile(c,(3,1,1))
# print(d)


# try:
#     a = float(input('Enter the score: '))

#     if not (0.0 < a <= 1.0):
#         print('Please enter a value between 0.0 and 1.0')
#     elif a >= 0.9:
#         print('Grade: A')
#     elif a >= 0.8:
#         print('Grade: B')
#     elif a >= 0.7:
#         print('Grade: C')
#     else:
#         print('Grade below C')

# except ValueError:
#     print('Invalid input! Please enter a number.')


# def computepay(hours, rate):
#     if hours > 40:
#         regular_pay = 40 * rate
#         overtime_pay = (hours - 40) * 1.5 * rate
#         return regular_pay + overtime_pay
#     else:
#         return hours * rate

# try:
#     hours = float(input("Enter hours: "))
#     rate = float(input("Enter rate: "))

#     grosspay = computepay(hours, rate)
#     print(f"Gross pay:",grosspay)

# except ValueError:
#     print("Invalid input! Please enter numeric values for hours and rate.")

result = []
while True:
    number =input('enter a number')
    
    
    if number.upper() == "DONE":
        break
    try:
        n = int(number)
        result.append(n)
        print(result)
    except ValueError:
        print('enter a valid number')
print(result)
    
if result:
    print('largest number',max(result))
    print('smallest numer',min(result))
else:
    print('No numbers are entered ')


