with open("one-hundred_fifty-digit_numbers.txt","r") as f:
	
	sum = 0

	for line in f:
		sum += int(line[0:50])
	print(str(sum)[0:10])


