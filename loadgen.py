
#!/usr/bin/python
"""
Generate load on a web server using simple get requests
"""  
import sys
import gevent
from gevent import pool
from gevent import monkey


#monkey.patch_all()

import collections
import os
#import tempfile
import time
import urllib2

POOL_SIZE = 5000 # number of concurrent sessions
MAX_SESSIONS = 10000 # total number of sessions to test


if len(sys.argv) > 1:
#  _REQUESTS = [(j, x) for j, x in enumerate(list(str(sys.argv)), 1) if j > 2]
  _REQUESTS = str(sys.argv[1])
else:
  _REQUESTS = [
      ('http://jradd.com/', None),
      ]

start = time.time()
tic = lambda: 'at %1.1f seconds' % (time.time() - start)

request_stats = collections.defaultdict(list)

def record_request(url, start, finish):
    """ Store request start/stop time into a global stats dict. """
    global threads
    threads = [request_stats[url].append((start, finish))]
    gevent.joinall(threads)

request_pool = pool.Pool(POOL_SIZE)
q_sessions = 0 
while q_sessions < MAX_SESSIONS:
    q_sessions += 1
    print('Testing: {0}'.format(_REQUESTS))
    print('tic: %s' % tic())
    print('Queued: %d' % q_sessions)
    print('toc: %s' % tic())
request_pool.join()
stop_time = (start - time.time())
print('Time: %s' % stop_time)

