"""
Problem 4

"""
def is_palindrome(n):
  """
  Okay, so this isn't really the "right" way where
  you keep dividing modulo 10 and ensuring the most
  and least significant digit are the same at each 
  step, but its quick enough to do the job here
  and its also just two lines.
  """
  ns = str(n)
  return ns == ns[::-1]

if __name__ == "__main__":
  mx = 0;
  for i in xrange(100, 1000):
    for j in xrange(100, 1000):
      n = i * j
      mx = n if n > mx and is_palindrome(n) else mx
  print mx
