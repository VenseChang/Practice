def longest_common_prefix(strs)
  return "" if strs.length <= 0
  return strs[0] if strs.length == 1
  str = ""
  strs[0].each_char.each_with_index {|val, index| (!strs.map{|str_val| str_val[index] == val }.include? false)? str += val : break}
  return str
end