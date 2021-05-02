#pip3 install -U pip setuptools
#pip3 install --upgrade kiteconnect
import logging
from kiteconnect import KiteConnect

logging.basicConfig(level=logging.DEBUG)

# Enter api_key, api_secret and request_token in the below variables
login_key = ""
login_secret = ""
request_token = ""
kite = KiteConnect(api_key = login_key)

# Redirect the user to the login url obtained
# from kite.login_url(), and receive the request_token
# from the registered redirect url after the login flow.
# Once you have the request_token, obtain the access_token
# as follows.

#Python code to get login_url
#kite = KiteConnect(api_key = login_key)
#kite.login_url()

data = kite.generate_session(request_token, api_secret = login_secret)
kite.set_access_token(data["access_token"])
