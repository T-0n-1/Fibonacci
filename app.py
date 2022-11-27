def fibonacciSeq(steps: int, oldSum: int =1, sum: int =0) -> list:
 """
 Function  for computing Fibonacci sequence
 :param steps: (int) steps to take in Fibonacci sequence
 :param oldSum: (int) earlier number in Fibonacci sequence
 :param sum: (int) current number in Fibonacci sequence
 :return: (list) of numbers aka Fibonacci sequence
 """
 if steps < 1:
  return [sum]
 else:
  steps -= 1
  oldSum, sum = sum, sum + oldSum
  return [oldSum] + fibonacciSeq(steps, oldSum, sum)


print(fibonacciSeq(10))