# tests for lab07, UCSB, CMPSC 8

import pytest
from lab07 import *

'''
	You should write your own test cases using pytest. 
	Here are some examples. 
'''

def test_canWeMakeIt_1():
	assert canWeMakeIt("tim", "iamtheta") == True

def test_canWeMakeIt_2():
	assert canWeMakeIt("ggezgame", "gotosleep") == False

def test_getWordPoints_1():
	assert getWordPoints("abc", {'a' : 1, 'b' : 2, "c" :3}) == 6

def test_getWordPoints_1():
	assert getWordPoints("roast", {'a' : 21, 'b' : 20, "c" :30, "o" : 90, "r" : 42, "s" : 140, "t" : 127}) == 420



# Add more tests below



if __name__ == '__main__':
   pytest.main(["./lab07_tests.py", "--capture=sys"])
