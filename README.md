# GooglebotDiscord
A Discord bot that scrapes data from Google searches. It uses the parameters (the rest of the message besides "google" at the start of it)
and pastes them to Google's URL

This was written in Python 3.6, so I cannot guarantee it will work on other versions as well. I believe versions prior to 3.5
require some tweaking to work, due to discord.py working a bit differently in these versions.

The project requires an installation of discord.py, and importing asyncio and Scraper.py. Scraper.py requires bs4 and requests to be installed and imported.

## Installing discord.py

To install the library without full voice support, you can just run the following command:

```
python3 -m pip install -U discord.py
```

Otherwise to get voice support you should run the following command:

```
python3 -m pip install -U discord.py[voice]
```

More info on https://github.com/Rapptz/discord.py


## Beautiful Soup
You can find information about Beautiful Soup here: https://www.crummy.com/software/BeautifulSoup/
