import os
level=1
x=level+1
right = True
playing = True
scores = [0]

while playing == True:
	os.system("clear")
	try:
		while right == True:
			print("#=====> LEVEL "+str(level)+" <=====#")
			n=level+1
			print(str(x)+" x "+str(n)+" = ?")
			entry = int(input(":"))
			if entry == x*n:
				scores.append(x)
				x = x*n
			else :
				right = False
			os.system("clear")
		print("the answer was: "+str(x*n))
		print("Do you wish to continue?")
		entry = input("(y/n):")
		if entry[:1] == "y":
			level+=1
			x=level+1
			right=True
		else:
			final_score=0
			for score in scores:
				final_score += score
			os.system("clear")
			print("TOTAL SCORE")
			print("!!! "+str(final_score)+" !!!")
			print("Thanks for playing.")
			exit()
	except:
		exit()


