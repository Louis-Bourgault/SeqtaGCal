import get_classes
from dotenv import load_dotenv
import os
import datetime
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def main():
    # If modifying these scopes, delete the file token.json.
    SCOPES = ["https://www.googleapis.com/auth/calendar"]

    load_dotenv()

    baseurl = os.getenv('BASEURL')
    print(baseurl)
    url = baseurl + '/#?page=/timetable'

    username = os.getenv('SEQTA_USERNAME')
    print(username)
    password = os.getenv('PASSWORD')

    classes = get_classes.getClasses(url, username, password)
    def parse_time(time_string):
        first_part = time_string.split(':')[0]
        length = len(first_part)
        second_part = time_string[length:length+3]
        start_time = first_part + second_part

        length = len(time_string)

        second_half = time_string[length-5:]
        if second_half[0] == '1':
            return [start_time, second_half]
        else:
            return [start_time, second_half[1:]]
        
    def add_event(class_name, room, teacher, start, end, date):
        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json')
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        try:
            service = build('calendar', 'v3', credentials=creds)        

        except HttpError as e:
            print('I SPY A BIG FAT ERROR OOPSIE DOOPSIE WHAT WENT WRONG I WONDER')
            print(e)
        event = {
            'summary': class_name,
            'location': room,
            'description': teacher,
            'start': {
                'dateTime': f'{date}T{start}:00+08:00',
                'timeZone': 'Australia/Perth',
            },
            'end': {
                'dateTime': f'{date}T{end}:00+08:00',
                'timeZone': 'Australia/Perth',
            },
        }
        print(event)
        event =  service.events().insert(calendarId=os.getenv('GOOGLE_CALENDAR_ID'), body=event).execute()
        print('Event created: %s' % (event.get('htmlLink')))

    for class_ in classes:
        #print(class_)
        time = class_['times']
        [start, end] = parse_time(time)
        print(f"{class_['name']} starts at {start} and ends at {end}")
        add_event(class_['name'], class_['room'], class_['teacher'], start, end, class_['date'])


if __name__ == '__main__':
    main()
