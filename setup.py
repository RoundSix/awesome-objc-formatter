#!/bin/env python
# -*- coding: utf-8 -*-

import shutil
import os


def setup():
  target_folder = os.path.abspath(os.path.dirname(os.getcwd()))
  shutil.copyfile('./.clang-format.bak', target_folder + '/.clang-format')


if __name__ == '__main__':
  setup()
