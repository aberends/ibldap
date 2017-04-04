#!/usr/bin/python

import ldap3

CUSER_DN       = 'cn=Directory Manager'
PEOPLE_DN      = 'ou=people,dc=prorail,dc=nl'
cuser_password = 'redhat123'
local_ldap     = 'ldap1.home.org'
install        = 'allard'
password       = 'redhat123'


s = ldap3.Server(local_ldap)
c = ldap3.Connection(s, user=CUSER_DN, password=cuser_password)
c.open()
c.start_tls()
c.bind()
install_dn = 'uid=%s,%s' % (install, PEOPLE_DN)
c.modify(
  install_dn,
  {
    'passwordexpirationtime': [(ldap3.MODIFY_REPLACE, ['20170402170000Z'])],
    'nsroledn':               [(ldap3.MODIFY_REPLACE, [])]
  }
)
print c.result
c.unbind()
