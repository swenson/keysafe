#!/usr/bin/env python
import json
import subprocess as sp
import sys

TEMP = 'tempout'

status_json, _ = sp.Popen('keybase status', stdout=sp.PIPE, shell=True).communicate()
status = json.loads(status_json)
user = status['user']['name']

inp = sys.argv[1]
blob = json.load(open('%s.encrypted' % inp))
s = blob[user]
with open(TEMP, 'w') as fout:
  fout.write(s)
sp.check_call('keybase decrypt --batch %s | less' % TEMP, shell=True)
