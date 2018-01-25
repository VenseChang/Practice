def climb_stairs(n)
  nums = [0, 1, 2]
  while nums.size - 1 <= n
    nums << nums[nums.size - 1] + nums[nums.size - 2]
  end
  nums[n]
end