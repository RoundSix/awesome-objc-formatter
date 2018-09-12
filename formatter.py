#!/bin/env python
# -*- coding: utf-8 -*-

import os
import utils.logger as logger
from utils import common
from subprocess import Popen, PIPE, run
from abc import ABCMeta, abstractmethod


class FormatterInterface(object):
  __metaclass__ = ABCMeta

  @abstractmethod
  def format(self, files):
    pass


class DryFormatter(FormatterInterface):

  def format(self, files):
    logger.info('Start check...')

    ret = []
    for file in files:
      command = [
        './bin/checker',
        file
      ]
      shell_ret = Popen(command, shell=False, stdout=PIPE)
      lines = shell_ret.stdout.readlines()
      diff_count = int(str(lines[0], encoding='utf-8').strip('\n'))
      if diff_count > 0:
        ret.append(file + ' ' + str(diff_count))

    if len(ret) > 0:
      logger.warn(str(len(ret)) + ' Files need to be formatted\n')
      for file_name in ret:
        logger.info(file_name)
    else:
      logger.info('Great! No file need to be formatted')


class WetFormatter(FormatterInterface):

  def format(self, files):
    logger.info('Start format...')
    for file in files:
      command = [
        './bin/formatter',
        file
      ]
      run(command)


def start(all_file: bool, dry_run: bool):
  if all_file:
    files_to_be_checked = common.all_objc_files(os.path.abspath(os.path.dirname(os.getcwd())))
  else:
    # change working directory and execute svn status to get all changed subversion files
    # and then change the working directory back
    current_folder = os.getcwd()
    os.chdir(os.path.dirname(current_folder))
    files_to_be_checked = common.subversion_objc_files_to_check()
    os.chdir(current_folder)

  if dry_run:
    formatter = DryFormatter()
  else:
    formatter = WetFormatter()

  formatter.format(files_to_be_checked)
