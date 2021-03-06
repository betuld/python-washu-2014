def binarify(num): 
  """convert positive integer to base 2"""
  if num<=0: return '0'
  digits = []
  powers = [2048,1024,512,256,128,64,32,16,8,4,2,1]
  for i in powers:
  	digits.append(str(num / i))
  	num %=  i
  return ''.join(digits)	
  
def int_to_base(num, base):
  """convert positive integer to a string in any base"""
  if num<=0:  return '0'
  digits = []
  for i in range(13,-1,-1):
  	power = base**i
  	digits.append(str(num / power))
  	num %=  power
  return ''.join(digits)

def base_to_int(string, base):
  """take a string-formatted number and its base and return the base-10 integer"""
  if string=="0" or base <= 0 : return 0 
  result = 0
  power=range(len(string)-1,-1,-1)
  for i in range (0,len(string)):
  	result+=int(string[i])*(base**power[i])
  return result 

def flexibase_add(str1, str2, base1, base2, baseOUT):
  """add two numbers of different bases and return the sum"""
  out = base_to_int(str1,base1) + base_to_int(str2, base2)
  return int_to_base(out, baseOUT) 

def flexibase_multiply(str1, str2, base1, base2,baseOUT):
  """multiply two numbers of different bases and return the product"""
  out = base_to_int(str1,base1) * base_to_int(str2, base2)
  return int_to_base(out, baseOUT)
  
def romanify(num):
  """given an integer, return the Roman numeral version"""
  result = []
  first=['','I','II','III','IV','V','VI','VII','VIII','IX']
  second=['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
  third=['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
  fourth=['','M','MM','MMM']
  result.append(fourth[num / 1000])
  num %= 1000
  result.append(third[num / 100])
  num %= 100
  result.append(second[num / 10])
  num %= 10
  result.append(first[num])
  return ''.join(result)
  


