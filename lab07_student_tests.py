# tests for lab07, UCSB, CMPSC 8

import pytest
'''
	You should write your own test cases using pytest. 
	Here are some examples. 
'''

from lab07 import createWordList

def test_createWordList_0():
  assert False


def test_createWordList_1():
  assert False

from lab07 import canWeMakeIt

def test_canWeMakeIt_0():
  assert(canWeMakeIt('ape','pae') == True)

def test_canWeMakeIt_1():
  assert(canWeMakeIt('ape','pael') == True)


#You will write your own test cases. 

if __name__ == '__main__':
   pytest.main(["lab07_student_tests.py", "--capture=sys"])
