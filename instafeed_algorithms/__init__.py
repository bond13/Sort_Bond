import mergesort
import quicksort
import bubblesort
import radixsort

_ALGORITHMS = [
    ("Quicksort (IF)", "Ave O(nlogn), Worst O(n^2)", quicksort),
    ("Mergesort (IF)", "O(nlogn)", mergesort),
    ("Bubblesort (IF)", "O(n^2)", bubblesort),
    ("Radixsort (IF)", "O(kn)", radixsort)]
