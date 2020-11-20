import numpy as np

board = np.array([["-","-","-"],
					["-","-","-"],
					["-","-","-"]])

win = [[1,2,3],
		[4,5,6],
		[7,8,9],
		[1,4,7],
		[2,5,8],
		[3,6,9],
		[1,5,9],
		[3,5,7]]
		
p1moves = []
p2moves = []

lisp1 = []
lisp2 = []

ct=0

def checkwin(pmoves,lisp,win):
	winner=0
	winning=[]
	li = []
	for x in pmoves:
		li.append(x)
		for n in pmoves:
			if n in li:
				li = [x]
				continue
			else:
				li.append(n)
				for j in pmoves:
					if j in li:
						li = [x,n]
						continue
					else:
						li.append(j)
					li.sort()
					if li in lisp:
						pass
					else:
						if len(li)<3:
							pass
						else:
							lisp.append(li)
					li = [x,n]
			li = [x]
		li = []
	
	for m in lisp:
		if m in win:
			winner=1
			winning=m
			break
		else:
			winner=0
			
	return lisp,pmoves,winner,win,winning
	
turn=1
winner=0

print("\nTic-Tac-Toe\nTo play your move, enter a number from 1-9.")
print()
print(board)
print()

while ct<9:
	try:
		print("P1 moves so far: {}".format(p1moves))
		print("P2 moves so far: {}".format(p2moves))
		player = int(input("P{}: ".format(turn)))
	except:
		print("Invalid choice.")
		continue
	else:
		pass
		
	if 0<player<4:
		row = 0
		cell = player-1
	elif 4<=player<7:
		row = 1
		cell = player-4
	elif 7<=player<10:
		row = 2
		cell = player-7
	else:
		print("Invalid choice.")
		continue
		
	if board[row][cell] != "-":
		print("Invalid choice.")
		continue
		
	ct+=1
		
	if turn == 1:
		p1moves.append(player)
		board[row][cell] = "X"
		print()
		print(board)
		print()
		lisp1,p1moves,winner,win,winning = checkwin(p1moves,lisp1,win)
		if winner==1:
			print("P1 wins!\nSet: {}".format(winning)")
			quit()
		else:
			turn=2
			continue
	elif turn == 2:
		p2moves.append(player)
		board[row][cell] = "O"
		print()
		print(board)
		print()
		lisp2,p2moves,winner,win,winning = checkwin(p2moves,lisp2,win)
		if winner==1:
			print("P2 wins!\nSet: {}".format(winning))
			quit()
		else:
			turn=1
			continue
		
print("Draw!\n")
