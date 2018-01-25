def valid(str)
  if ['{', '(', '['].include? str
    case str
      when '{'
        @right << '}'
      when '('
        @right << ')'
      when '['
        @right << ']'
    end
    @left << str
  else
    if @right.empty?
      return false
    else
      @left << @right.pop
    end
  end
end

def is_valid(s)
  return false if s.length % 2 != 0 or ['}', ')', ']'].include? s[0]
  @left, @right =  [], []
  s.each_char{|val| return false if !valid(val)}  
  (s == (@left+@right.reverse).inject(:+))? true : false
end