result = list(map(lambda x: "fizzbuzz" if x%15 == 0 else "fizz" if x%5 == 0 else "buzz" if x%3 ==0 else x, [i for i in range(1, 101)]))

for i in range(1, 101):
    if (i%3 == 0 or i%5 == 0):
        print("fizz" * (i%3 == 0) + "buzz" * (i%5 == 0))
    else:
        print(i)

print(list(map(
    lambda x:'fizzbuzz' if x % 15 == 0 else 'fizz' if x % 3 == 0 else 'buzz' if x % 5 == 0 else x,
    range(1, 100 +1))))

# jaemin
# func = lambda x: "fizzbuzz" if x%15==0 else "fizz" if x%3==0 else "buzz" if x%5==0 else x
# print(*map(func, range(1,101))

