# SeqtaGCal
 Simple utility to push seqta timetable entries to your Google calendar for easier access.


This is a simple utility that I made myself for my own personal use. If you find it useful, that's cool! The code is rather janky and some things REALLY aren't perfectly implemented, but it works.

## Usage
This repo includes a .env.sample file. Copy it, rename it to .env, and populate it with your own variables.
You will also need a copy of the chrome webdriver for your operating system in the same directory, and Google Chrome installed on your machine. Name this chromedriver.exe.
To integrate with Google calendar, credentials are required. Make an oauth consent screen on Google Cloud Platform, and enable the calendar API. Instructions can be found on the Google Calendar API quickstart page for python.

To run this in the background, I reccomend adding this to Cron to run weekly

Thanks for using!

## Possible additions
Since this is a purely functional project, I might not add these. If anyone wants to do it though, a PR would be much appreciated!
- When it is run again in the same week, itll add duplicate events to your google calendar. To resolve this, fetch google calendar events first. This would be useful for if the timetable is modified midweek and you need to run more than once to cope with updates.