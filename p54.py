hands=open('p054_poker.txt').readlines()
count=0

card_values={'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'T':9,'J':10,'Q':11,'K':12,'A':13}

def counter(x):
	tempdic={}
	for i in x:
		if i in tempdic:
			tempdic[i]+=1
		else:
			tempdic[i]=1
	return(tempdic)

def parse_hands(line):
	line=line.split(' ')
	line=[(i[0],i[1]) for i in line]
	c_values=([card_values[i[0]] for i in line ])
	suits=[i[1] for i in line]
	p1=(c_values[:5],suits[:5])
	p2=(c_values[5:],suits[5:])

	return p1,p2 

def value_hand(hand):
	print(hand)
	if check_straight(hand[0]) and check_flush(hand[1]) and sorted(hand[0])[0]==9:
		return(10)
	elif check_straight(hand[0]) and check_flush(hand[1]):
		return 9
	elif check_four_of_kind(hand[0]):
		return 8
	elif check_full_house(hand[0]):
		return 7
	elif check_flush(hand[1]):
		return 6
	elif check_straight(hand[0]):
		return 5
	elif check_three_of_kind(hand[0]):
		return 4
	elif check_two_pair(hand[0]):
		return 3
	elif check_pair(hand[0]):
		return 2
	else:
		return 1

def check_pair(x):
	if len(counter(x))==4:
		return True

def check_two_pair(x):
	if len(counter(x))==3:
		if sorted(counter(x).values())==[1,2,2]:
			return True

def check_three_of_kind(x):
	if len(counter(x))==3:
		if sorted(counter(x).values())==[1,1,3]:
			print(3)
			return True

def check_four_of_kind(x):
	if len(counter(x))==2:
		if sorted(counter(x).values())==[1,4]:
			return True

def check_full_house(x):
	if len(counter(x))==2:
		if sorted(counter(x).values())==[2,3]:
			return True

def compare_hands(p1,p2):
	global count
	print(p1)
	print(p2)
	value1=value_hand(p1)
	value2=value_hand(p2)
	if value1>value2: 
		count+=1
		print(count)
	elif value1==value2: 
		if value1 in [2,3,4,7,8]:
			d1=counter(p1[0])
			d2=counter(p2[0])
			print()
			h_card=(sorted([sorted(d1.items(),key=lambda x: x[1],reverse=True),sorted(d2.items(),key=lambda x: x[1],reverse=True)],reverse=True))
			if h_card[0]==sorted(d1.items(),key=lambda x: x[1],reverse=True):
				count+=1
				print(count)
		else: 
			d1=sorted(p1[0],reverse=True)
			d2=sorted(p2[0],reverse=True)
			print()
			h_card=(sorted([d1,d2],reverse=True))
			if h_card[0]==d1:
				count+=1
				print(count)
		#print('2')
	print('\n')

def check_straight(x):
	x=sorted(x)
	if x[0]+4==x[1]+3==x[2]+2==x[3]+1==x[4]:
		return True

def check_flush(x):
	if x[0]==x[1]==x[2]==x[3]==x[4]:
		print('flush')
		return True

for line in hands[:]:
	print(line)
	p1,p2=parse_hands(line)
	compare_hands(p1,p2)

print(count)