def is_same_tree(p, q)
  return true if p == nil and q == nil
  return false if p == nil or  q == nil
  return (is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)) if p.val == q.val
  return false
end