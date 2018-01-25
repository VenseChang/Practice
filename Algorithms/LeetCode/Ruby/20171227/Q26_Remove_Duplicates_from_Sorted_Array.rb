# @param {Integer[]} nums
# @return {Integer}
def duplicates ary
  nums = []
  ary.each{|val| nums << val if !nums.include? val}
  return nums
end

def remove_duplicates(nums)
  i = 0
  ary = duplicates(nums)
  while nums != ary
    (nums[i] == nums[i+1])? nums.delete_at(i) : i+=1
  end
  return nums.size
end