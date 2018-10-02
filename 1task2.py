"""create a new configuration file that start with '172.' and '192." to "10." 
and also change the security-level to "10" . """

def change_ip(file_name):
	file=open(file_name)
	lstA=[]
	lstB=[]	#contains all ip address
	lstC=[]	#contains list of elements in ip add
	lstD=[]	#list of updated ip add  
	for line in file:
		line=line.strip()
		for word in line.split():
			lst.append(word)
	for i in range(len(lst)):
		if lstA[i-1]!='no' and lstA[i]=='ip' and lstA[i+1]=='address':
			lst2.append(lstA[i+2])	
	for i in lstB:
		lst3.append(i.split('.'))	#list of elements in ip
	for i in lstC:		
		del i[0]	#del first element
		i.insert(0,'10')	
		lstD.append('.'.join(i))
	return lstD

print(change_ip('running-config.txt'))
