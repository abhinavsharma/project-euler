h = 0
(100..999).each do |i|
  (100..999).each  do |j|
    p = i * j
    h = [h, p].max if p.to_s == p.to_s.reverse
  end
end
puts h
