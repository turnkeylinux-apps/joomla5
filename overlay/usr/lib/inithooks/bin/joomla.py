#!/usr/bin/python3
"""Set Joomla admin password and email

Option:
    --pass=     unless provided, will ask interactively
    --email=    unless provided, will ask interactively

"""

import sys
import getopt
from libinithooks import inithooks_cache
import random
import string
import hashlib

from libinithooks.dialog_wrapper import Dialog
from mysqlconf import MySQL

def usage(s=None):
    if s:
        print("Error:", s, file=sys.stderr)
    print("Syntax: %s [options]" % sys.argv[0], file=sys.stderr)
    print(__doc__, file=sys.stderr)
    sys.exit(1)

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass=', 'email='])
    except getopt.GetoptError as e:
        usage(e)

    password = ""
    email = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            password = val
        elif opt == '--email':
            email = val

    if not password:
        d = Dialog('TurnKey Linux - First boot configuration')
        password = d.get_password(
            "Joomla Password",
            "Enter new password for the Joomla 'admin' account.")

    if not email:
        if 'd' not in locals():
            d = Dialog('TurnKey Linux - First boot configuration')

        email = d.get_email(
            "Joomla Email",
            "Enter email address for the Joomla 'admin' account.",
            "admin@example.com")

    inithooks_cache.write('APP_EMAIL', email)

    salt_chars = string.ascii_letters + string.digits
    salt = "".join(random.choice(salt_chars) for c in range(32))
    cryptpass = "%s:%s" % (hashlib.md5((password + salt).encode('utf8')).hexdigest(), salt)

    m = MySQL()
    m.execute('UPDATE sites_joomla.j_users SET email=%s WHERE username=\"admin\";', (email,))
    m.execute('UPDATE sites_joomla.j_users SET password=%s WHERE username=\"admin\";', (cryptpass,))

if __name__ == "__main__":
    main()

