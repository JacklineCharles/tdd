import unittest
from tdd import solution
class TestSolution(unittest.TestCase):
	def test_addition(self):
		self.assertTrue(solution(10,20, "+"),30)
	def test_addition(self):
		self.assertTrue(solution(10,20, "*"),200)
	def test_addition(self):
		self.assertTrue(solution(20,10, "/"),2)
	def test_addition(self):
		self.assertTrue(solution(30,20, "-"),10)		


if __name__=="__main__":
	unittest.main()
