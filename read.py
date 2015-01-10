#!/usr/bin/env python
import json
import subprocess as sp
import sys

TEMP = 'tempout'

with open(os.path.join(os.ennviron['HOME'], '.keybase', 'config.json')) as statusf:
  status = json.load(statusf)
  user = status['user']['name']

inp = sys.argv[1]
if inp.endswith('.encrypted'):
  inp = inp[:-10]
blob = json.load(open('%s.encrypted' % inp))
s = blob[user]
with open(TEMP, 'w') as fout:
  fout.write(s)
#sp.check_call('keybase decrypt --batch %s | less' % TEMP, shell=True)
sp.check_call('gpg decrypt %s' % )
