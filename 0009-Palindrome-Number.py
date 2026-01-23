class solution: 
  def palindrome (slef,x: int)-->
  #if the given number is negative then it"s not a plaindrome, for example if the given number is -121 then the reverse is 121- is not a palindrome.
  if x<0:
    return False
  return str(x) == str(x)[::-1] #this ia magic suntax used to reverse the number
