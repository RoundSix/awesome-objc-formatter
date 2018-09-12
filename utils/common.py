#!/bin/env python
# -*- coding: utf-8 -*-

import os

valid_objc_file_postfix = ['.h', '.m', '.hh', '.mm']


def get_ignored_directories():
  ret = []
  if os.path.isfile('.formatting-directory-ignore'):
    file_reader = open('.formatting-directory-ignore', 'r')
    for line in file_reader.readlines():
      ret.append(line.strip('\n'))
    file_reader.close()

  return ret


def all_objc_files(path):
  objc_files = []
  ignored_directories = get_ignored_directories()

  for root, dirnames, files in os.walk(path):
    dirnames[:] = [
      dirname for dirname in dirnames
      if not dirname.startswith('.') and dirname not in ignored_directories]
    files[:] = [
      file for file in files
      if not file.startswith('.') and os.path.splitext(file)[-1] in valid_objc_file_postfix]

    for file in files:
      objc_files.append(os.path.join(root, file))

  return objc_files


def subversion_objc_files_to_check():
  folder = os.getcwd()
  # command below should assemble dynamically
  command = "svn status | awk '{print $2}' | grep -e '\.m$' -e '\.mm$' -e '\.h$' -e '\.hh$'"
  process = os.popen(command)
  output = process.read()
  process.close()

  files = output.split()

  ignored_directories = get_ignored_directories()
  ret = []
  for file in files:
    dirs = os.path.splitext(file)
    ignore = False

    for dir_name in dirs:
      if dir_name in ignored_directories:
        ignore = True
        break

    if not ignore:
      ret.append(folder + '/' + file)

  return ret
