def reverse(x)
     return (x.to_s.reverse.to_i > 2**31-1) ? 0 : (x >= 0) ? x.to_s.reverse.to_i : x.abs.to_s.reverse.to_i*-1
end
