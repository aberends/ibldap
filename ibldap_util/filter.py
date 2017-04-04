#!/usr/bin/python

import sys

def correct_parentheses(a):
  if a[0] != '(':
    a = '(%s' % (a,)
  if a[-1] != ')':
    a = '%s)' % (a,)
  return a
  
def and_filter(*arg):
  if len(arg) < 2:
    print >> sys.stderr, '%(module)s, %(function)s: %(error)s' % {
      'module':   __name__,
      'function': sys._getframe().f_code.co_name,
      'error':  'specify at least 2 arguments',
    }
    sys.exit(1)
  f = '(&%s%s)' % (correct_parentheses(arg[0]), correct_parentheses(arg[1]))
  for i in arg[2:]:
    f = '(&%s%s)' % (correct_parentheses(i), f)
  return f

def not_filter(a):
  return '(!%s)' % (a,)

def or_filter(a, b):
  return '(|%s%s)' % (a, b)


if __name__ == "__main__":
  pass
