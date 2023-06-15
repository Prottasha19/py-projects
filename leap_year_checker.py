#!/bin/python
#version 1.1

import sys

def is_leap_year(year):
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				print('{} Year is a leap year'.format(year))
			else:
				print('{} Year is not a leap year'.format(year))	
		else:
			print('{} Year is a leap year'.format(year))
	else:
		print('{} Year is not a leap year'.format(year))
		
#""" year = int (input("Write a year: ")) """

year = int(sys.argv[1]) #version 1.1
is_leap_year(year)
