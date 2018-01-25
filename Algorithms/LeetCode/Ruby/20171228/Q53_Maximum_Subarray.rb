def max_sub_array(nums)
  max_value, num = nums[0], 0
  nums.each do |val|
    num += val
    max_value = num if num > max_value
    num = 0 if num < 0
  end
  max_value
end