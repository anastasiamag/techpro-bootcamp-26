# print("another program")
# for i in range(10,0,-1):
#     print(i)
#for i in range(10):
# print(10-i)

# # FizzBuzz
# for i in range(1,21):
#     if(i%3== 0 and i%5==0):
#         print("FizzBuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     else: 
#         print(i)

# #Intro to functions
# age =10 
# def hello(name):
#     print(f"Hello {name}")

# def greeting(name):
#     return f"Hello {name}"


# name="jimmy"
# greeting("Anastasia")

# hello("Anastasia")

# factorial
def factorial(n):
    result =1
    if n==1:
        return 1
    for i in range(2, n+1):
        result*=i
    return result

print(factorial(3))
print(factorial(4))
print(factorial(0))
print(factorial(1))
print(factorial(5))


