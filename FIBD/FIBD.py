def fib(m1, m2=1):
  ages = [1] + [0]*(m2 - 1)
  for i in range(m1 - 1):
    ages = [sum(ages[1:])] + ages[:-1]
  return sum(ages)
print(fib(80,16))