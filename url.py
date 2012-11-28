from url_normalize import url_normalize

class URL:
  # Initializes URL object with source and normalized version
  def __init__(self, url):
    self.url = url
    self.normalized = url_normalize(url)

  # Url is valid if source matches normalized
  def isValid(self):
    return self.url == self.normalized

  # Returns normalized version of url
  def getNormalized(self):
    return self.normalized
  
  # Returns length of url
  def __len__(self):
    return len(self.normalized)

  # Returned an index of normalized url
  def __getitem__(self, index):
    return self.normalized[index]

  # Comparison using normalized url
  # URLs are compared first on validity
  # Next compared using string operator of the normalized URLs
  def __lt__(self, other):
    if self.isValid() != other.isValid():
      return self.isValid > other.isValid()
    else:
      return self.normalized < other.normalized

  def __le__(self, other):
    if self.isValid() != other.isValid():
      return self.isValid > other.isValid()
    else:
      return self.normalized <= other.normalized

  def __gt__(self, other):
    if self.isValid() != other.isValid():
      return self.isValid < other.isValid()
    else:
      return self.normalized > other.normalized

  def __ge__(self, other):
    if self.isValid() != other.isValid():
      return self.isValid < other.isValid()
    else:
      return self.normalized >= other.normalized

  def __eq__(self, other):
    if self.isValid() != other.isValid():
      return False
    else:
      return self.normalized == other.normalized
