from os import system
import Utils as u

#~ l = [8, 6, 1, 4, 2, 9, 10]
l = [3,7,8,5,2,1,9,5,4]
n = len(l)
u.quick_sort(l,0,n-1)
print(l)


system("Pause")
