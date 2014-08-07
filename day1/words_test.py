<<<<<<< HEAD
import unittest
import words

class TestWordsCode(unittest.TestCase):

  def test_has_no_e(self):
    self.assertEqual(words.has_no_e("bet"), False)
    self.assertEqual(words.has_no_e("bit"), True)

  def test_uses_only(self):
    self.assertEqual(words.uses_only("ababab", "a"), False)
    self.assertEqual(words.uses_only("ababab", "ab"), True)

  def test_uses_all(self):
    self.assertEqual(words.uses_all("ababab", "abc"), False)
    self.assertEqual(words.uses_all("ababab", "ab"), True)

  def test_is_abecedarian(self):
    self.assertEqual(words.is_abecedarian("abcxyz"), True)
    self.assertEqual(words.is_abecedarian("abczyx"), False)
=======
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
>>>>>>> 9fbd2da1721a4d81392d8a699a39bedb13a86fa9
