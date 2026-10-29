# print("another program")
# for i in range(10,0,-1):
#     print(i)
#for i in range(10):
# print(10-i)

# FizzBuzz
for i in range(1,21):
    if(i%3== 0 and i%5==0):
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else: 
        print(i)