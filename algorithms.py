import instafeed_algorithms
import full_house_algorithms

_IF_algs = instafeed_algorithms._ALGORITHMS
_FH_algs = full_house_algorithms._ALGORITHMS
_algs = _IF_algs + _FH_algs

def RunAlgorithm(index, urls):
  module = _algs[index][2]
  return module.sort(urls)

def GetAlgorithms():
  return [tup[:2] for tup in _algs]
