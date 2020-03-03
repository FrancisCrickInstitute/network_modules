#!/usr/bin/env python
'''
With no arguements will look for environment variables for username, tacacs+ password
and single sign-on password. If not found it will prompt for username and tacacs+ password
only.
Use -o if environment variables are defined, but you don't wish to use them (e.g. lab)
-s means it will also prompt for an SSO password, say for API calls
'''
from argparse import ArgumentParser
from getpass import getpass
import os

def get_creds():
    parser = ArgumentParser(description='Usage:')
    parser.add_argument('-u', '--username', type=str,
                        help='Username [OPTIONAL]')
    parser.add_argument('-p', '--password', type=str,
                        help='Tacacs+ Password [OPTIONAL]')
    parser.add_argument('-s', '--sso_password', action='store_true',
                        help='Enable Single Sign-On Password Input [OPTIONAL]')
    parser.add_argument('-o', '--override', action='store_true',
                        help='Override Stored Credentials and allow manual input only')
    args = parser.parse_args()
    output = {}
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
    # This section happens with no args at all
    else:
        ENV_user_un = input('Your Username: ')
        ENV_user_pw = getpass('Your Tacacs+ Password: ')
    # SSO Password
    if args.sso_password == True:
        if args.override == False:
            try:
                ENV_user_sp = os.environ['PY_USER_SP']
            except:
                ENV_user_sp = getpass('Your SSO Password: ')
        else:
            ENV_user_sp = getpass('Your SSO Password: ')
        output['sso_password'] = ENV_user_sp
    output['username'] = ENV_user_un
    output['tac_password'] = ENV_user_pw
    return output

