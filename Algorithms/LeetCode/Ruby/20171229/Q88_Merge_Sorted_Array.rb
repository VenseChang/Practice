def merge(nums1, m, nums2, n)
  j, k = n-1, m+n-1
  while j > -1
    nums1[k] = nums2[j]
    j -= 1
    k -= 1
  end
  nums1.sort!
end