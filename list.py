my_list = []
#appending
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#insert 
my_list.insert(1, 15)
#extend with values 50 60 70
my_list.extend([50, 60, 70])
#remove the last element from my list
my_list.pop()
#sorting my list in ascending order
my_list.sort()
#find and print index of the value 30
index_30 = my_list.index(30)
print("index of 30 in my_list:", index_30)