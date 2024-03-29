"""

  The main function. Assume all characters are in ASCII.

"""

import sys, random
import algorithms

from url import URL

def get_strings(f):
  strings = []
  line = f.readline()
  while len(line) > 0:
    # do not add empty line
    if len(line) > 1:
      strings.append(line[:len(line) - 1])
    line = f.readline()
  return strings

if __name__ == "__main__":

  filename = None
  if len(sys.argv) not in (3,4):
    print 'Usage: python main.py [--valid|--invalid] input-file output-file'
    exit(1)

  inputfile = None
  if len(sys.argv) == 3:
    inputfile = open(sys.argv[1])
  else:
    # If optional flag is set
    inputfile = open(sys.argv[2])

  strings = get_strings(inputfile)
  validFlag = -1
  urls = [URL(x) for x in strings]
  sourceDict = dict()
  normalDict = dict()
  for x in urls:
    if sourceDict.has_key(x.url):
      sourceDict[x.url]+=1
    else:
      sourceDict[x.url]=1
    if normalDict.has_key(x.normalized):
      normalDict[x.normalized]+=1
    else:
      normalDict[x.normalized]=1
  validUrls = [x for x in urls if x.isValid()]
  invalidUrls = [x for x in urls if not x.isValid()]
  if len(sys.argv) == 4:
    if sys.argv[1] == '--valid':
      validFlag = 1   
    else:
      validFlag = 0

  algorithm_tuples = algorithms.GetAlgorithms()
  print 'Which sorting algorithm would you like?'
  for (i, tup) in enumerate(algorithm_tuples):
    print str(i) + ") " + tup[0] + ". Runtime: " + tup[1]


  option = None
  while option is None or (option >= len(algorithm_tuples) or option < 0):
    sorting_method = raw_input('Enter an option number: ')
    try:
      option = int(sorting_method)
      if option < 0 or option >= len(algorithm_tuples):
        raise ValueError('Option out of range')
    except ValueError:
      print 'Invalid input %s. Please enter the integer before each option.' % sorting_method
  
  outputfile = None
  if len(sys.argv) == 3:
    outputfile = open(sys.argv[2], 'w+')
  else:
    outputfile = open(sys.argv[3], 'w+')
  validResults = algorithms.RunAlgorithm(option, validUrls)
  invalidResults = algorithms.RunAlgorithm(option, invalidUrls)
  if validFlag == -1 or validFlag == 1:
    for item in validResults:
      outputfile.write('%s\n' % item.url)
  if validFlag == -1 or validFlag == 0:
    for item in invalidResults:
      outputfile.write('%s\n' % item.url) 
  for item in urls:
    print ('Source: %s' % item.url)
    print ('Valid: %s' % item.isValid())
    print ('Canonical: %s' % item.normalized)
    print ('Source unique : %s' % (sourceDict[item.url]==1))
    print ('Canonicalized URL unique : %s\n' % (normalDict.has_key(item.normalized) and normalDict[item.normalized]==1))
  print 'Sorting with \'%s\' successfully.\n' %option
  inputfile.close()
  outputfile.close()
