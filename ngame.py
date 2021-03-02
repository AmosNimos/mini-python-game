
level=1
x=level+1
right = True
playing = True
scores = [0]

while playing == True:
	print("#=====> LEVEL "+str(level)+" <=====#")
	try:
		while right == True:
			print(str(x)+" x "+str(level+1)+" = ?")
			entry = int(input(":"))
			if entry == x*2:
				scores.append(x)
				x = x*2
			else :
				right = False
		print("the answer was: "+str(x*2))
		print("Do you wich to continue?")
		entry = input("(y/n):")
		if entry[:1] == "y":
			level+=1
			x=level+1
			right=True
		else:
			final_score=0
			for score in scores:
				final_score += score
			print("TOTAL SCORE")
			print("!!! "+str(final_score)+" !!!")
			print("thanks for playing.")
			exit()
	except:
		exit()


