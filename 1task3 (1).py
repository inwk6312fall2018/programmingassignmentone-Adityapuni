"""function to create a list of "access-list" for "global_access" and "fw-management_access_in"""

def access_list(right_n):
	file=open(right_n)
	lst=[]
	for line in file:
		line=line.strip()
		for i in line.split():	#
			if i=='global_access' or i=='fw-management_access_in':
				list.append(line)
	return list
print(access_list('running-config.cfg')		
