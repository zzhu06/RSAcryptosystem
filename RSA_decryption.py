#RSA system is hard to Break, because 
#it is hard/impossible to break a product into two large prime numbers

#Only the receiver knows the private key: (n,d)
#d is the inverse of e=13 mod phi(2537)
#phi(2537) = phi(43*59) = 42*58 = 2436 
d = 937; n = 2537

#I am the letter dictionary. Nothing magic here 
def letterdict():
	dict ={}
	num = 0 
	for i in 'abcdefghijklmnopqrstuvwxyz'.upper():
		if num < 10: 
			dict[i] = '0'+str (num)
			num += 1
		else: 
			dict[i] = str (num)
			num += 1
	return dict
letterdict = letterdict()

#I am opening the magic box! 
#I can decrypt the message, because I know the private key (n,d)
def decipher(listOfNumbers): 
	res = []
	for num in listOfNumbers: 
		newNum = str(int(num)**d%n)
		if len(newNum)<4: 
			newNum = '0'* (4-len(newNum)) + newNum
		res.append(newNum)
	return res
#Test Me: delete '#' on next line and compile
#print decipher(['0981', '0724', '0709', '1230', '1333', '0288'])

#Not yet! 
#I change the decrypted numbers into original message
def decipherText(listOfNumbers): 
	Text = []
	for i in range(len(listOfNumbers)):
		Text.append(letterdict.keys()[letterdict.values().index(listOfNumbers[i][:2])])
		Text.append(letterdict.keys()[letterdict.values().index(listOfNumbers[i][2:])])
	Text = ''.join(Text)
	return Text
#Test Me: delete '#' on next line and compile
#print decipherText(decipher(['0981', '0724', '0709', '1230', '1333', '0288']))


