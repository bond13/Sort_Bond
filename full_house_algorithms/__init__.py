import mergesort
import heapsort
import selectionsort 
import radixsort

_ALGORITHMS = [ 
    ("Heapsort (FH)", "Ave O(nlogn)", heapsort),
    ("Mergesort (FH)", "O(nlogn)", mergesort),
    ("Selectionsort (FH)", "O(n^2)", selectionsort),
    ("Radixsort (FH)", "O(kn)", radixsort)]
