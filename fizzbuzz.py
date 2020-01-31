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

# jaemin
#func = lambda x: "fizzbuzz" if x%15==0 else "fizz" if x%3==0 else "buzz" if x%5==0 else x
#prnt(*map(func, range(1,101))
#result = list(map(lambda x: "fizzbuzz" if x%15 == 0 else "fizz" if x%5 == 0 else "buzz" if x%3 ==0 else x, [i for i in range(1, 101)]))

# for i in range(1, 101):
#    if (i%3 == 0 or i%5 == 0):
#        print("fizz" * (i%3 == 0) + "buzz" * (i%5 == 0))
#    else:
#        print(i)
#
#print(list(map(
#    lambda x:'fizzbuzz' if x % 15 == 0 else 'fizz' if x % 3 == 0 else 'buzz' if x % 5 == 0 else x,
#    range(1, 100 +1))))

# jaemin
# func = lambda x: "fizzbuzz" if x%15==0 else "fizz" if x%3==0 else "buzz" if x%5==0 else x
# print(*map(func, range(1,101))

range_number = range(0,101)
#print(list(map(lambda x: 'fizzbuzz' if x % 15 == 0 else 'fizz' if x % 3==0 else 'buzze' if  x % 5==0 else x, range_number)))

for i in range_number:
    print('fizz'* (not(i%3)) + 'buzz' * (not(i%5)) or i )
    print(('fizz'* (not(i%3)) + 'buzz' * (not(i%5))), i )
f
