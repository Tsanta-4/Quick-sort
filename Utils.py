def quick_sort(tab, start, last):
	"""Fonction tri rapide"""
	if start <= last:
		pivot = last
		pivot = partition(tab, start, last, pivot)
		quick_sort(tab, start, pivot-1)
		quick_sort(tab, pivot+1, last)

def partition(tab, start, last, pivot):
	"""fonction qui permet de partitionner les sous-tableau"""
	tab[pivot], tab[last] = tab[last], tab[pivot]
	j = start
	for i in range(start, last):
		if tab[i] <= tab[last]:
			tab[i], tab[j] = tab[j], tab[i]
			j += 1
	tab[last], tab[j] = tab[j], tab[last]
	return j
	
