# Heap sort
from heapq import heappush, heappop

def sort(urls):
    size = len(urls)
    heap = []
    for i in range(size):
        heappush(heap, urls.pop(0))
    for i in range(size):
        urls.append(heappop(heap))
    return urls
