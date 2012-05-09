# Problem 3

import sys

def largest_prime_factor(n):
  i = 2
  factors = {}
  while i <= n:
    while n % i == 0:
      n = n / i
      if i in factors:
        factors[i] += 1
      else:
        factors[i] = 1
    i += 1
  return factors

if __name__ == "__main__":
  print max(largest_prime_factor(int(sys.argv[1])))
