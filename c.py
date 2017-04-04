#!/usr/bin/python

import datetime
import ldap3

CUSER_DN       = 'cn=Directory Manager'
PEOPLE_DN      = 'ou=people,dc=prorail,dc=nl'
cuser_password = 'redhat123'
local_ldap     = 'ldap1.home.org'
install        = 'allard'
password       = 'redhat123'

now_string = datetime.datetime.now().strftime('%Y%m%d%H%M%SZ')

# What are we searching for?
# All entries with uid=install_vos or uid=install_beheer*.
# And of those entries the ones that have no
# passwordexpirationtime or whose passwordexpirationtime is
# in the past and is not inactivated.
# (&(|(uid=install_vos)(uid=install_beheer*))(|(!(passwordexpirationtime=*))(passwordexpirationtime<="now")))

def and_filter(a, b):
  return '(&%s%s)' % (a, b)

def not_filter(a):
  return '(!%s)' % (a,)

def or_filter(a, b):
  return '(|%s%s)' % (a, b)

search_filter = and_filter(
  and_filter(
    or_filter(
      '(uid=%s)' % ('install_vos',),
      '(uid=%s)' % ('allard',)
    ),
    or_filter(
      not_filter('(passwordexpirationtime=*)'),
      '(passwordexpirationtime<=%s)' % (now_string,)
    )
  ),
  not_filter('(nsroledn=*)')
)

s = ldap3.Server(local_ldap)
c = ldap3.Connection(s, user=CUSER_DN, password=cuser_password)
c.open()
c.start_tls()
c.bind()
install_dn = 'uid=%s,%s' % (install, PEOPLE_DN)
c.search(
  search_base   = PEOPLE_DN,
  search_filter = search_filter,
  search_scope  = ldap3.LEVEL,
  attributes    = [ldap3.ALL_ATTRIBUTES]
)

for e in c.response:
  print e
  print

c.unbind()
