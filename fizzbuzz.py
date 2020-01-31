# jaemin
func = lambda x: "fizzbuzz" if x%15==0 else "fizz" if x%3==0 else "buzz" if x%5==0 else x
prnt(*map(func, range(1,101))
