def test_has_no_e(self):
	return "e" in self
	
def test_uses_only(self,letters):
	self=self.lower()
	letters=letters.lower()
	test=[]
	for i in range(0,len(self)):
		if self[i] in letters:
			test.append(1)
	return sum(test)==len(self)
	
def test_uses_only(self,letters):
	test=[]
	for i in range(0,len(letters)):
		if letters[i] in self:
			test.append(1)
	return sum(test)==len(letters)		
		
def test_is_abecedarian(self):
	self=self.lower()
	for i in range(0,len(self)-1):
		if self[i]<=self[i+1]:
			continue
		else:
			return False
	return True