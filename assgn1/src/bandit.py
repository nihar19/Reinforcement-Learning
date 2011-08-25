#!/bin/python
from random import gauss

class Bandit:
	def __init__(self):
		self.arms = []

	# Setup the bandit experiments
	def setupBandit(self, noOfArms):
		for i in range(noOfArms):
			self.arms.append(Arm(gauss(0,1), 1, i))
	
	def resertBandit(self):
		for arm in self.arms:
			arm.meanEstimate = 0

# Assuming arm always samples according to a gaussian distribution
class Arm:
	def __init__(self, mean, variance, index):
		self.mean = mean
		self.variance = variance

		self.noOfPlays = 0
		self.meanEstimate = 0

	def sample(self):
		return gauss(self.mean, self.variance)
