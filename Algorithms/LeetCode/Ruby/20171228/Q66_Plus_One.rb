def plus_one(digits)
  return digits.size if digits.size == 0
  len, sum = digits.size - 1, 0
  digits.each do |val|
    sum += val * 10 ** len
    len -= 1
  end
  sum += 1
  digits = []
  sum.to_s.each_char {|val| digits << Integer(val)}
  digits
end