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

from pyhelm.chartbuilder import ChartBuilder
from pyhelm.tiller import Tiller

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
    namespace = get_parameter(query, 'namespace', False)
    version = get_parameter(query, 'version', False)

    #chart = ChartBuilder({'name': 'blue-green-app', 'source': {'type': 'directory', 'location': '../blue-green-app'}})
    #chart.install_release(chart.get_helm_chart(), dry_run=False, namespace='default')

    sys.stdout.write(json.dumps({
        'namespace': 'Hello Apps',
        'version': "0.1"
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
