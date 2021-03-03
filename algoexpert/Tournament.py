def tournamentWinner(competitions, results):
	winners = dict()
	count = 0
	highest = None
	winner = None

	for item in competitions:
		result = results[count]
		team = None

		if result == 0:
			team = item[1]
		else:
			team = item[0]

		if team not in winners:
			winners[team] = 3
		else:
			winners[team] += 3

		if highest is None or winners[team] > highest:
			highest = winners[team]
			winner = team

		count += 1
	
	#for key,value in winners.items():
	#	if highest is None or value > highest:
	#		highest = value
	#		winner = key
	
	print(winners)
	return winner


if __name__ == "__main__":
	competitions = [
		["html", "C#"],
		["C#", "Python"],
		["Python", "html"]
	]
	results = [0, 0, 1]

	print(tournamentWinner(competitions, results))
