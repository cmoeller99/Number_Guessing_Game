import random

query = int(input("guess a number:"))
a = random.randint(1,10)
i = 1
guess = []
while query != a:
	print (f'Sorry,{query} is not correct') 
	print (f' that was try:{i}')
	guess.append(query)
	print(f'your previously guessed {guess}')
	query= int(input("guess again:"))
	i +=1

	
print(f'{query} is correct!!!! it took you {i} guesses')



