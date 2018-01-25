def add_value_to_list(l)
  while l != nil
      @merge_list << l.val
      l = l.next
  end
end

def merge_two_lists(l1, l2)
  @merge_list = []
  add_value_to_list l1
  add_value_to_list l2
  @merge_list.sort
end