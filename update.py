#!/usr/bin/env python
import json
import os.path
import subprocess as sp

TEMP = 'tmptmptmp'

def encrypt_single(file, user):
  print 'Encrypting %s for user %s' % (file, user)
  sp.check_call('keybase encrypt -o %s %s %s' % (TEMP, user, file), shell=True)

def encrypt(file, users):
  blob = {}
  for user in users:
    encrypt_single(file, user)
    with open(TEMP) as tempin:
      data = tempin.read()
      blob[user] = data
  with open(file + '.encrypted', 'w') as out:
    json.dump(blob, out)

for file, users in json.load(open('acl.json')).iteritems():
  if os.path.exists(file):
    encrypt(file, users)
