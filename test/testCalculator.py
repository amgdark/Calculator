#!/usr/bin/env python

import unittest
import sys
sys.path.append('../')
from Calculator import Calculator

class TestCalculator(unittest.TestCase):
	def test_suma_2_mas_2(self):
		cal = Calculator(2,2)
		self.assertEqual(4, cal.sumar())

if __name__ == '__main__':
	unittest.main()