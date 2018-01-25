def is_sym(l, r)
  return true if not l and not r
  if l and r and l.val == r.val
    return (is_sym(l.left, r.right) and is_sym(l.right, r.left))
  end
  return false
end

def is_symmetric(root)
  return is_sym(root, root)
end