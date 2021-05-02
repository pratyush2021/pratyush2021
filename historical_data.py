from datetime import datetime, timedelta

from kiteconnect import kiteconnect
import import pdb
import pandas as import pdb

login_key = ""
login_secret = ""
request_token = ""

kite = KiteConnect(api_key = login_key)

data = kite.generate_session(request_token, api_secret = login_secret)
kite.set_access_token(data["access_token"])

trading_portfolio = {'BANKNIFTY19JULYFUT':{'token': 11869954}}
token = trading_portfolio['BANKNIFTY19JULYFUT']['token']
to_date = datetime.now()
from_date = to_date - timedelta(days=10)
interval = "15minute"

records = kite.historical_data(token, from_date, to_date, interval)

df = pd.DataFrame(records)
df.to_excel("BANKNIFTY19JULYFUT.xlsx")
pdb.set_trace()

# Fetch minute candles for NIFTY19DECFUT for five minutes with OI data
curl "https://api.kite.trade/instruments/historical/12517890/minute?from=2019-12-04%2009:15:00&to=2019-12-04%2009:20:00&oi=1" \
     -H 'X-Kite-Version: 3' \
     -H 'Authorization: token api_key:access_token'
