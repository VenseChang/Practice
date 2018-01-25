def compute(s)
  len, num = s.length - 1, 0
  s.each_char do |val|
    num += 2 ** len * val.to_i
    len -= 1
  end
  return num
end

def add_binary(a, b)
  n1, n2 = compute(a), compute(b)
  num = n1 + n2
  ans = ""
  if num != 0
    while num != 0
      ans << (num % 2).to_s
      num /= 2
    end
  else
    ans << "0"
  end
  return ans.reverse
end