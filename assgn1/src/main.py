from bandit import Bandit
from random import choice

def main():
	bandit = Bandit()
	bandit.setupBandit(10)
	
	for i in range(1000):
		greedyPlay(bandit, 500)
	

def greedyPlay(bandit, noOfPlays):
	totalReward = 0

	for i in range(noOfPlays):
		armPlayed = choice(getGreedyArms(bandit))
		pullArm(armPlayed, totalReward)

	averageReward /= float(noOfPlays)

def epsilonGreedyPlay(bandit, e, noOfPlays):
	totalReward = 0

	for i in range(noOfPlays):
		if(random() <= e):
			armPlayed = choice(bandit.arms)
		else:
			armPlayed = choice(getGreedyArms(bandit))

		pullArm(armPlayed, totalReward)

	averageReward /= float(noOfPlays)


def getGreedyArms(bandit):
	greedyArms = [bandit.arms[0]]
	for arm in bandit.arms:
		if arm.meanEstimate > greedyArms[0].meanEstimate:
			greedyArms = [arm]
		elif arm.meanEstimate == greedyArms[0].meanEstimate:
			greedyArms.append(arm)

	return greedyArms

def pullArm(arm, totalReward):
	arm.noOfPlays += 1
	reward = arm.sample()

	totalReward += reward

	factor = float(armPlayed.noOfPlays - 1)/armPlayed.noOfPlays
	armPlayed.meanEstimate = armPlayed.meanEstimate * factor + reward/armPlayed.noOfPlays
	

if __name__ == '__main__':
	main()
