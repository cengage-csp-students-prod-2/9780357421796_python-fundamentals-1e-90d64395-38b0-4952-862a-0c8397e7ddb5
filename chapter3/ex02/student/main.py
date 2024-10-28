#python3_year = 2008
#year = int(input('When was Python3 first released?'))

#if year == python3_year:
#	print(bool(python3_year))
#	print('Correct')
#else:
#	print(False)
#	print('Incorrect')
#	print('Have a great day!')

answer = (input('Return True or False: Python3 was released in 2008: '))
answer = answer.capitalize()
if answer == 'True':
	print('Correct.')
elif answer == 'False':
    print('Incorrect.')
else:
	print('Please answer True or False')
print("Have a great day!")