for i in range(1, 100+1):
    print("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or i)


#for i in range(1, 101):
#    if i % 3 == 0:
#        print("3의 배수입니다 : fizz")
#    if i % 5 == 0:
#        print("5의 배수입니다 : buzz")
#    if i % 15 == 0:
#        print("15의 배수입니다 : fizzbuzz")

# result = ["fizzbuzz" if i%15==0 else 
#     "fizz" if i%3==0 else 
#     "buzz" if i%5==0 else 
#     i for i in range(1,100+1)
#     ]

# print(result)

