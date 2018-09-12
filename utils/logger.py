#!/bin/env python
# -*- coding: utf-8 -*-


class AnsiColors:
  SUCCESS = '\033[0;32m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'


def info(log_info):
  print(log_info)


def success(log_info):
  print(AnsiColors.SUCCESS + log_info + AnsiColors.ENDC)


def warn(log_info):
  print(AnsiColors.WARNING + log_info + AnsiColors.ENDC)


def error(log_info):
  print(AnsiColors.FAIL + log_info + AnsiColors.ENDC)
