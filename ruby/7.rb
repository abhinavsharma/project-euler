require 'mathn'
n = 1
Prime.new.each do |i|
  if n == 10001
    puts "the #{n} prime is #{i}"
    break
  end
  n += 1
end
