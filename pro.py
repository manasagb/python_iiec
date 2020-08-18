import os

while True:
	inp = input()

	if ('not' in inp or "don't" in inp or 'dont' in inp) and ('chrome' in inp or 'notepad' in inp or 'vlc' in inp or 'km' in inp or 'player' in inp or 'editor' in inp):
		print("Ok fine :)")

	elif ('run' in inp or 'load' in inp or 'execute' in inp or 'launch' in inp) and ('chrome' in inp):
		os.system('chrome')

	elif ('run' in inp or 'load' in inp or 'execute' in inp or 'launch' in inp) and (('notepad' in inp) or ('editor' in inp)):
		os.system('notepad')

	elif ('run' in inp or 'load' in inp or 'execute' in inp or 'launch' in inp) and ('vlc' in inp or 'vlc player' in inp):
		os.system('start vlc')
	
	elif ('run' in inp or 'load' in inp or 'execute' in inp or 'launch' in inp) and ('kmplayer' in inp or 'km player' in inp):
		os.system('start kmplayer')

	elif ('exit' in inp):
		break
	
	else:
		print("Not supporting :(")
