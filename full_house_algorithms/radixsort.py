# Radix sort

def sort(urls):
    # If it's empty don't bother sorting.
    if (not urls):
      return urls
    # Make a temp list since I can't lose the reference to urls.
    temp = list(urls)
    maxlen = max(map(lambda url: len(url), temp))
    for i in range(maxlen, -1, -1):
      chars =  [[] for j in range (0, 256)] # Create a bucket for each char.
      for url in temp:
          # Grab the int value of the char or 0 if no char.
          charindex = ord(url[i]) if i < len(url) else 0
          chars[charindex].append(url)
      temp = [item for sublist in chars for item in sublist] # flatten
    # Copy the values back into the original list.
    for i in range(0, len(urls)):
      urls[i] = temp[i]
    return urls
