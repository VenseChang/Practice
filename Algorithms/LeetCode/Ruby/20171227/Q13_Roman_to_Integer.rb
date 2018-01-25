def roman(s)
  case s
        when 'M'
            1000
        when 'D'
            500
        when 'C'
            100
        when 'L'
            50
        when 'X'
            10
        when 'V'
            5
        when 'I'
            1
    end
end

def roman_to_int(str)
  nums = []
  str.each_char { |s| nums << roman(s) }
  nums.each_with_index{ |val, index| nums[index] *= -1 if nums[index] < nums[index+1] if index < nums.length-1  }
  nums.sum
end