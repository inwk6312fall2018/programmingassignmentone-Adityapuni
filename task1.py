""" THIS IS THE FUNCTION RETURN A LIST OF  (INTERFACE NAME nameif VALUE"""
def int_and_int_name(file_name):
	file=open(file_name)
	listA=[]
	listB=[]	#INTERFACE 
	listC=[]	#INTERFACE NAME
	listD=[]	#TUPLE (interface,interface name)
	for line in file:
		line=line.strip()
		for word in line.split():
			list1.append(word)	# WILL MAKE A LIST OF ALL WORDS
	for i in range(len(listA)):
		if listA[i]=='interface':
			listB.append(list1[i+1])	#MAKE LIST OF INTERFACE
		elif listA[i]=='nameif' or (listA[i]=='no' and listA[i+1]=='nameif'):
			#MAKE LIST OF INTERFACE NAME AS WELL
			if listA[i]=='no' and listA[i+1]=='nameif':
				listC.append('no name')
			elif listC[i-1]!='no' and listA[i]=='nameif':
				listC.append(listA[i+1])
	for i in range(len(listB)):			#CREATE LIST OF TUPLE(INTERFACE,INTERFACE NAME)
		listD.append((listB[i],listC[i]))
	return listD

"""THIS FUNCTION CHANGE THE CONFIGURATION AND RETURN A DICTIONARY CONTAINING "interfacce" AS A KEY and "NAMEIF,VLAN,IPADDRESS,SUBNET MASK"
 LIST AS THE CORRESPONDING VALUES""""

def list_ifname_ip(file_name):
	file=open(file_name)
	listA=[]
	listB=[]	#INTERFACE LIST
	listC=[]	#NAME OF INTERFACE
	listD=[]	#VLAN ID
	listE=[]	# IP ADDRESS
	listF=[]	#SUBNETMASK
	listG=[]	#LIST OF INTERFACE NAME,VLANID,IP ADDRESS,SUBNETMASK
	dict={}	#DICTIONARY
	for line in file:
		line=line.strip()
		for word in line.split():
			listA.append(word)
	for i in range(len(listA)):
		if listA[i]=='interface':
			listB.append(listA[i+1])  #MAKING LIST OF INTERFACE
		elif listA[i]=='nameif' or (listA[i]=='no' and listA[i+1]=='nameif'):
			#MAKING A LIST OF INTERFACE NAME
			if listA[i]=='no' and listA[i+1]=='nameif':
				listC.append('no name')
				listD.append('no vlan')	#FOR THE INTERFACE WHICH HAS NO NAME , NO IP ADDRESS AND NO SUBNETMASK
				list5.append('no ip address')
				listE.append('no netmask')
			elif listA[i-1]!='no' and listA[i]=='nameif':
				listC.append(listA[i+1])
				listE.append(listA[i+6])
				listF.append(listA[i+7])
				if listA[i-1]=='management-only':	# MANAGEMENT NETWORK CAS
					listD.append('no vlan')
				else:
					listD.append(listA[i-2]+listA[i-1])
	for i in range(len(list2)):
		lisG=[]
		listG.append(list3[i])
		listG.append(list4[i])
		listG.append(lst5[i])
		listG.append(lst6[i])
		dict[listB[i]]=listG	#add list of nameif,ip,netMask as value in dict
	return dict


print('List contain tuple interface (interfacename,"nameif"- value) is:\n',int_and_int_name('running-config.cfg'))
print('dictionary that contains the "interfacename" as the key and "nameif,VLAN,IPaddress,NetMask" list as the value is :\n',list_ifname_ip('running-config.cfg'))
