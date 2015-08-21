# coding: utf-8


'''
for i in range(2000,3200):
	if i % 7 == 0:
		if i % 5 != 0:
			print(i)
'''
		
print ([i for i in range(2000,3200) if i % 7 == 0 and i % 5 != 0])

