# SeqtaGCal
 Simple utility to push seqta timetable entries to your Google calendar for easier access.


This is a simple utility that I made myself for my own personal use. If you find it useful, that's cool! The code is rather janky and some things REALLY aren't perfectly implemented, but it works.

## Usage
This repo includes a .env.sample file. Copy it, rename it to .env, and populate it with your own variables.
You will also need a copy of the chrome webdriver for your operating system in the same directory, and Google Chrome installed on your machine. Name this chromedriver.exe.
To integrate with Google calendar, credentials are required. Make an oauth consent screen on Google Cloud Platform, and enable the calendar API. Instructions can be found on the Google Calendar API quickstart page for python.

Thanks for using