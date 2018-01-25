def search_insert(nums, target)
  nums << target
  nums = nums.sort
  nums.index target
end