def compute(str)
  origin_str, strs, counter = str[0], [], []
  str.each_char.each_with_index do |val, index|
    if val != origin_str
      strs << "#{counter.size}#{counter[0]}"
      counter, origin_str = [], val
      counter << val
    else
      counter << val
    end
  end
  strs << "#{counter.size}#{counter[0]}"
  strs.inject(:+)
end

def count_and_say(n)
  step, str = 1, "1"
  while step != n
    str = compute(str)
    step += 1
  end
  return str
end