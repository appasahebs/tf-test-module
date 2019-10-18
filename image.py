#!/usr/bin/env python

from __future__ import print_function
import boto3
import json
import os
import sys
if (sys.version_info > (3, 0)):
    import urllib.request as urllib
else:
    import urllib2 as urllib

credentials = None

def error(message):
    print(message, file=sys.stderr)
    sys.exit(1)


def get_parameter(query, key, required=True):
    value = query.get(key)
    if value is None:
        if required:
            error('Query parameter %s is required.' % key)
        value = ''
    return value

def image():
    query = json.loads(sys.stdin.read())
    namespace = get_parameter(query, 'namespace')
    version = get_parameter(query, 'version')
    sys.stdout.write(json.dumps({
        'namespace': namespace,
        'version': 0.1
    }))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        error('Missing first argument')
    if sys.argv[1] == 'image':
        try:
            image()
        except Exception as ex:
            # data "external" is only prepared for a one line message.
            error('%s: %s' % (type(ex), ex))
    else:
        error('Unexpected first argument: %s' % sys.argv[1])
