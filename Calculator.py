#!/usr/bin/env python

class Calculator:
	def __init__(self, a, b):
		self.__a=a
		self.__b=b

	def sumar(self):
		return self.__a+self.__b

	def restar(self):
		return self.__a-self.__b

	def multiplicar(self):
		return self.__a*self.__b

	def dividir(self):
		if self.__b!=0:
			return self.__a/self.__b
		else:
			return "Error, division entre cero"
	
	
