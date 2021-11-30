"""A module for talking about Teddy's age"""
from random import randint

def how_old():
	age = randint(20, 201)

	return f'Teddy is {age} years old!'