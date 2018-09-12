#!/bin/env python
# -*- coding: utf-8 -*-

import sys
import getopt
import os
import re
import codecs
import formatter
import utils.logger as logger


def usage():
  """
  Usage: awesome-objc-formatter.py [-a][-c][-h|--help][-v|--version]

  Description: ☞
  -a            Check all files and echo file names which should be formatted
  -c            Check those files changed in Subversion and echo file names which should be formatted. The value should be true or false
  -h,--help     Show help info
  -v,--version  Show version info
  """


def version():
  """
  ---- awesome-objc-formatter ----
  ----          %(v)s          ----
  ---- awesome-objc-formatter ----
  """


def read(*parts):
  here = os.path.abspath(os.path.dirname(__file__))
  with codecs.open(os.path.join(here, *parts), 'r') as fp:
    return fp.read()


def find_version():
  here = os.path.abspath(os.path.dirname(__file__))
  with codecs.open(os.path.join(here, './__version__.py'), 'r') as fp:
    version_file = fp.read()

  version_match = re.search(
    r"^__version__ = ['\"]([^'\"]*)['\"]",
    version_file,
    re.M,
  )
  if version_match:
    return version_match.group(1)

  raise RuntimeError('Unable to find version string')


def main():
  try:
    opts, args = getopt.getopt(sys.argv[1:], "achv", ["help", "version"])
  except getopt.GetoptError as err:
    logger.error(str(err))
    logger.error(usage.__doc__)
    sys.exit(1)

  if sys.version_info[0] < 3:
    raise RuntimeError('awesome-objc-formatter require python 3')

  format_all = False
  dry_run = False

  for o, a in opts:
    if o in ("-h", "--help"):
      logger.success(usage.__doc__)
      sys.exit(0)
    elif o in ("-v", "--version"):
      version_string = find_version()
      logger.success(version.__doc__ % {'v': version_string})
      sys.exit(0)
    elif o == "-a":
      format_all = True
    elif o == "-c":
      dry_run = True

  formatter.start(format_all, dry_run)


if __name__ == "__main__":
  main()
