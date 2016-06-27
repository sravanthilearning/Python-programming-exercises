'''

ex4arraymapping.py

Turn single-spaced numbers from strings to arrays of integers and then compute the sum. 

'''

# [in] 6
# [in] 1 2 3 4 5 6
# [out] 21

n = input()
arr = map(int,raw_input().split()) #map integers to the strings.
print arr
print sum(arr)
