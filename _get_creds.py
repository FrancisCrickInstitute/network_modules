#!/usr/bin/env python

from argparse import ArgumentParser
from getpass import getpass

def get_creds():
    parser = ArgumentParser(description='Usage:')
    parser.add_argument('-u', '--username', type=str,
                        help='Username [OPTIONAL]')
    parser.add_argument('-p', '--password', type=str,
                        help='Password [OPTIONAL]')
    parser.add_argument('-o', '--override', action='store_true',
                        help='Override Stored Credentials and allow manual input only')
    args = parser.parse_args()

    if args.override == False:
        # Username
        if args.username is not None:
            ENV_user_un = args.username
        else: #is none
            try:
                ENV_user_un = os.environ['PY_USER_UN']
            except: # get here if no args given at all
                print("Override disabled but environment username or -u arg not provided")
                ENV_user_un = input('Your Username: ')
        # Password
        if args.password is not None:
            ENV_user_pw = args.password
        else: #is none
            try:
                ENV_user_pw = os.environ['PY_USER_PW']
            except:
                print("Override disabled but environment password or -p arg not provided")
                ENV_user_pw = getpass('Your Password: ')
        # Validation
        if ((ENV_user_un is None) or (ENV_user_pw is None)):
            print('ERROR: User Credentials Not Found!!!')
            sys.exit(0)
    else:
        ENV_user_un = input('Your Username: ')
        ENV_user_pw = getpass('Your Password: ')
    output = {}
    output['username'] = ENV_user_un
    output['password'] = ENV_user_pw
    return output
