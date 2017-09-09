#!/bin/python3

stairCaseDict = {0:1, 1:1}

def climbStairs(steps):
	global stairCaseDict
	if (steps < 0):
		return 0
	elif (steps == 0):
		return 1
	elif (steps == 1):
		return 1
	else:
		if (steps in stairCaseDict):
			return stairCaseDict[steps]
		else:
			stepCount = climbStairs(steps - 1) + climbStairs(steps - 2) + climbStairs(steps - 3)
			stairCaseDict[steps] = stepCount
			return stepCount

steps = 36
print(climbStairs(steps))