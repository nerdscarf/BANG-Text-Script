import os
import schedule
import time
from twilio.rest import Client
import yahoo_fin.stock_info as yfsi

## Twilio account authentificaiton
account_sid = '[TWILIO_ACCOUNT_SID]'
auth_token = '[TWILIO_AUTH_TOKEN]'

client = Client(account_sid, auth_token)

def text():
## Using Yahoo Fin, get the current price of a stock ##
bb = yfsi.get_live_price("BB") * [NUMBER OF SHARES YOU CURRENTLY HOLD AS AN INT OR FLOAT] 
amc = yfsi.get_live_price("AMC") * [NUMBER OF SHARES YOU CURRENTLY HOLD AS AN INT OR FLOAT]
nok = yfsi.get_live_price("NOK") * [NUMBER OF SHARES YOU CURRENTLY HOLD AS AN INT OR FLOAT]
gme = yfsi.get_live_price("GME") * [NUMBER OF SHARES YOU CURRENTLY HOLD AS AN INT OR FLOAT]

## Combines the returns of all the stocks
total_return = round(bb + amc + nok + gme, 2)

## Texts you using your Twilio number
    client.messages.create(
        to="[YOUR CELLPHONE NUMBER]",
        from_="[YOUR TWILIO NUMBER]",
        body="Your current total return is {}.".format(total_return)
)

# Schedules when the function executes
schedule.every().hour.at(":15").do(text)

while True:
    schedule.run_pending()
    time.sleep(1)