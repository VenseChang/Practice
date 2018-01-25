def two_sum(nums, target)
  dics = {}
  nums.each_with_index{|val, index| dics[target - val] = index}
  nums.each_with_index{|val, index| return [index, dics[val]] if dics[val] and dics[val] != index}
end
