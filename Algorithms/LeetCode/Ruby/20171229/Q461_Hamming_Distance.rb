def to_binary(num)
  str = []
  while num > 0
    str << num % 2
    num /= 2
  end
  return str
end

def hamming_distance(x, y)
  x, y = to_binary(x), to_binary(y)
  if x.size < y.size
    x, y = y, x
  end
  [*1..(x.size - y.size)].each{y << 0}
  count = 0
  x.each_with_index{|val, index| count += 1 if val != y[index]}
  return count
end