f1 = 1
f2 = 2
s = f2
f = f1 + f2
while f < 4000000
  if f % 2 == 0
    s += f
  end
  t = f1
  f1 = f2
  f2 = f2 + t
  f = f1 + f2
end
puts s
