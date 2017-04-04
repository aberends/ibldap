#!/usr/bin/python

import ibldap_util

# Get the necessary configuration parameters.
ADMIN_DN  = 'cn=Directory Manager'
ADMIN_PW  = 'redhat123'
PEOPLE_DN = 'ou=people,dc=prorail,dc=nl'
DS_FQDN   = 'ldap1.home.org'

# Build the search filter.
search = and_filter(
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

# Find LDAP accounts that meet the requirements to be locked.

# Loop over the accounts and lock them.


