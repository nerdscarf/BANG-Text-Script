# $BANG Stock Text Updates

## Description
This project is simple python script that will text you the estimated total return of your shares in Blackberry ($BB), AMC ($AMC), Nokia ($NOK), and Gamestop ($GME). I created this because I didn't want to spend all day tied to the news or a brokerage account waiting for updates on a single stock. This script will take the live value of each stock, multiply it by the number of shares you own, combine those values and text them to you once an hour.  
	
	
## Technologies
Project is created with:
* [Twilio’s API](https://www.twilio.com/)
* [Yahoo-fin](https://theautomatic.net/yahoo_fin-documentation/)
* [Schedule](https://schedule.readthedocs.io/en/stable/)


## Notes
This is not investment advice. Do you own due diligence and research. This script does not take into account your initial investment or options. 

## Making it work
* Create a free Twilio account to obtain your account sid, authentication token and phone number. Replace `[TWILIO_ACCOUNT_SID]`, `[TWILIO_AUTH_TOKEN]`, and `[YOUR TWILIO NUMBER]` with the corresponding information. 
* Add your share amounts. Replace `[NUMBER OF SHARES YOU CURRENTLY HOLD AS AN INT OR FLOAT]` with your share amount as and integer or float (#TeamFractionalShares)
* Add your cell phone number. Replace `[YOUR CELLPHONE NUMBER]` with your cellphone in +10123456789 format. 
		
		
## Only Live Price Mode
* If you would like this script to only text you the current live stock price remove `* [NUMBER OF SHARES YOU CURRENTLY HOLD AS AN INT OR FLOAT]` on lines 15 to 18, update line 21 to `total_return = bb + amc + nok + gme` and line 27 to `"Here are the current stock prices: BB {}, AMC {}, NOK {}, GME {}.".format(bb,amc,nok,gme)`.


## Customize The Time
* [Schedule's](https://schedule.readthedocs.io/en/stable/examples.html) documentation has great example code you can use to customize the timing of your text messages. All you need to do is replace `schedule.every().hour.at(":15").do(text)` on line 31 with your preferred text frequency. Be sure to update the do method with the name of the function `.do(text)`. 


## Deploy
I've included the `requirement.txt` and Procfile file that should hopefully help with deployment via Heroku. Push your code to Heroku and be sure to turn it on ([This YouTube video helped me](https://youtu.be/DwWPunpypNA?t=734)). Once you're done, be sure to check to make sure your app is up by checking `heroku logs`.


## Contact
Created by [@nerdscarf](https://www.twitter.com/nerdscarf) - feel free to contact me! [Donations](http://paypal.me/nerdscarf) are always welcome.
