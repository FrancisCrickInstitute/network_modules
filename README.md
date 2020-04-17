# network_modules
Modules used by the IT&amp;S Networks team

# Usage
Make sure you checkout this repo into a folder known by python. 
## One-time use example:
```
export PYTHONPATH=/Users/USERNAME/code/FrancisCrickInstitute-github/network_modules/
COMPUTERNAME:network_byod_audit USERNAME$ env | grep PYTHON
PYTHONPATH=/Users/USERNAME/code/FrancisCrickInstitute-github/network_modules/
```
## Permanent Solution osx example
```
vi ~/.bash_profile (use .bashrc for linux)
export PYTHONPATH="/Users/USERNAME/code/FrancisCrickInstitute-github/network_modules"
```

# _get_creds
Using a trival test script, test.py
```
  1 from _get_creds import get_creds
  2 
  3 foo = get_creds()
  4 print(foo)
``` 
Ensure your environment variables are defined:
```
HOST:network_modules morrelg$ export PY_USER_UN=testuser
HOST:network_modules morrelg$ export PY_USER_PW=env_pass123
HOST:network_modules morrelg$ export PY_USER_SP=env_sso456
```
Run without args to use environment variables for user and tacacs+ password:
```
HOST:network_modules morrelg$ python test.py 
{'username': 'testuser', 'tac_password': 'env_pass123'}
```
-o will mean it prompts you for these:
```
HOST:network_modules morrelg$ python test.py -o
Your Username: stdin_user
Your Tacacs+ Password: 
{'username': 'stdin_user', 'tac_password': 'stdin_pass'}
```
-s allows you to also enter an SSO password, e.g. for API calls:
```
HOST:network_modules morrelg$ python test.py -s
{'sso_password': 'env_sso456', 'username': 'testuser', 'tac_password': 'env_pass123'}
```
-o -s means everything is manual:
```
HOST:network_modules morrelg$ python test.py -o -s
Your Username: stin_user
Your Tacacs+ Password: 
Your SSO Password: 
{'sso_password': 'stdin_tacpass', 'username': 'stin_user', 'tac_password': 'stdin_pass'}
```
# _slack_post
Post to Slack using oath, allows for local file upload

This script results in two posts to Slack. The first is a direct image upload from a folder local to the script. The second is some text and an image crafted using https://api.slack.com/tools/block-kit-builder. 

The output is as follows:

![Output](https://github.com/guymorrell/slack-post-oath/blob/master/readme.png)

Both images sourced from https://ccsearch.creativecommons.org/search?q=slack&provider&li&lt=commercial&searchBy
