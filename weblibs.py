""" Simple Comparison/Reference between urllib2,urllib3 and requests. """
import time
import sys

# Constants
if len(sys.argv) > 1:
  _URL = str(sys.argv[1])
else:
  _URL = 'https://jradd.com'

_NUM = 100

def test_urllib2():
  from urllib2 import urlopen, HTTPError
  try:
    response = urlopen(_URL)
  except HTTPError as e:
    response.code
    return response.data

def test_requests():
  import requests
  s = requests.Session()
  response = s.get(_URL)
  response.status_code
  return response.content

if __name__ == '__main__':
  from timeit import Timer
  t_urllib2 = Timer("test_urllib2()", "from __main__ import test_urllib2")
  s = t_urllib2
  print("Requesting count: {0} from: {1}".format(_NUM, _URL))
  print("-" * 9)
  print("urllib2: {0}".format(s.timeit(number=_NUM)))
  t_requests = Timer("test_requests()", "from __main__ import test_requests")
  s = t_requests
  print("requests: {0}".format(s.timeit(number=_NUM)))
