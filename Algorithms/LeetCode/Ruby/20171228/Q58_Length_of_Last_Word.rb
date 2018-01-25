def length_of_last_word(s)
  strs = s.split(' ')
  (strs.size > 0)? strs[-1].length : 0
end