n = input()
l = ["a","e","i","o","u","A","E","I","O","U"]
if n.isnumeric() :
	print("invalid character")
elif n in l :
	print("vowel")
else :
	print("consonant")
 
