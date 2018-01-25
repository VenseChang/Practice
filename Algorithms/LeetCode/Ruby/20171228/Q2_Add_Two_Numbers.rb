def list_node_to_string(l)
  str = ""
  while l != nil
      str << l.val.to_s
      l = l.next
  end
  return str
end

def add_two_numbers(l1, l2)
  s1, s2 = list_node_to_string(l1), list_node_to_string(l2)
  i = s1.reverse.to_i + s2.reverse.to_i
  ans = []
  if i != 0
    while i != 0
      ans << i % 10
      i /= 10
    end
  else
    ans << 0
  end
  return ans
end