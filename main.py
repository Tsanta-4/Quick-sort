from os import system
import Utils as u
import time 

#~ l = [8, 6, 1, 4, 2, 9, 10]
#~ l = [3,7,8,5,2,1,9,5,4]
#~ l = [x for x in range(100000,-1,-1)]
l = [1]*100 + [2, 3, 43, 5, 7]
n = len(l)
start = time.time()
u.quick_sort(l,0,n-1)
end = time.time()
#~ print(l)
print("Temps d'execution = ", end-start)


system("Pause")
