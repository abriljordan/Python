# Write a python program which  accepts user’s first name and prints the unique characters of 
# the name on one line each, in ascending order, and in all caps.

first_name=input("Enter first name: ")

sorted_first_name = ''.join(sorted(first_name,key=str.lower))

for i in range(0, len(sorted_first_name)):
	flag=0
	for j in range(0, len(sorted_first_name)):
		if(first_name[i]==first_name[j] and i!=j):
			flag=1
			break
	if(flag==0):
		print(first_name[i].upper(),end="")