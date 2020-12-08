def quick_sort(tab, start, last):
	"""Fonction tri rapide"""
	if start <= last:
		pivot = partition(tab, start, last)
		quick_sort(tab, start, pivot-1)
		quick_sort(tab, pivot+1, last)

def partition(tab, start, last):
	"""fonction qui permet de partitionner les sous-tableau"""
	j = start
	pivot = tab[last]
	for i in range(start, last):
		if tab[i] <= pivot:
			tab[i], tab[j] = tab[j], tab[i]
			j += 1
	tab[last], tab[j] = tab[j], tab[last]
	return j
	
