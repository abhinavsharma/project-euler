# really just prime factorization using the prime sieve
require 'mathn'

n = 600851475143

Prime.new.each do |p|
  if n % p == 0
    n /= p
  end
  if n == 1
    puts p
    break
  end
end
