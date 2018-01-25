def delete_duplicates(head)
  nums = []
  while head != nil
    nums << head.val if !nums.include? head.val
    head = head.next
  end 
  return nums
end