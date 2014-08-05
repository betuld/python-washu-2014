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

class Clock():
	def __init__(self, hours, minutes):
		self.hours = hours
		self.minutes = minutes
# 		if self.hours >=24 or self.hours<0:
# 			return "This is NOT a time\!"
				
	@classmethod
	def at(cls, hours, minutes=0):
		return cls(hours,minutes)
	
	def __str__(self):
		if self.hours >= 10:
			hour = str(self.hours)
		elif self.hours <10:
			hour = "0" + str(self.hours)
		if self.minutes >=10:
			minute = str(self.minutes)
		elif self.minutes < 10:
			minute = "0" + str(self.minutes)
		return hour + ":" + minute
		
	def __add__(self, addminute):
		newminute = self.minutes + addminute
		addhour=0
		if newminute > 60:
			addhour = newminute/60
			newminute %= 60	
		newhour=self.hours+addhour	
		if newhour >23:
			newhour -= 24						
		return Clock(newhour,newminute)
	
			
	def __sub__(self, subminute):
		subhour = subminute/60
		subminute %= 60
		newminute = self.minutes-subminute
		newhour = self.hours-subhour
		if newminute < 0:
			newminute=60-abs(newminute)
			newhour -= 1 					
		if newhour < 0:
			newhour += 24
		return Clock(newhour,newminute)
		
		
	
	
print Clock.at(10)		
print Clock.at(10,3)
print Clock.at(10)+3	
print Clock.at(10)+61
print Clock.at(23, 30) + 60	
print Clock.at(10) - 90	
print Clock.at(0, 30) - 60	

				
# first_clock=Clock(8,2)
# second_clock=Clock(10,30)
# third_clock=Clock(-1,0)
# 
# print first_clock.at()
# print second_clock.at()
# print third_clock.at()
