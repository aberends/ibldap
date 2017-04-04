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
#c.start_tls()
c.bind()
# We use password modify operation of rfc3062. See section
# "Operation Requirements" of the RFC.
install_dn = 'uid=%s,%s' % (install, PEOPLE_DN)
if len(password) == 0:
  new_password = c.extend.standard.modify_password(install_dn, None, None, ldap3.HASHED_SALTED_SHA256)
  print 'Wachtwoord voor %s (buitenste quotes weghalen): "%s"' % (install, new_password)
else:
  c.extend.standard.modify_password(install_dn, None, password, ldap3.HASHED_SALTED_SHA512)
c.unbind()

