from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import telebot
from telebot import types

    
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SAMPLE_SPREADSHEET_ID = '1rn0leF5MYEAmsxmAHnodmkg7RBc7Ls0UIlCS79z1tnw'
SAMPLE_RANGE_NAME = 'RU!A1:T8'
creds = None



if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'creds.json', SCOPES)
        creds = flow.run_local_server(port=0)

    with open('token.json', 'w') as token:
        token.write(creds.to_json())

class Sheets:
    try:
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        
        values = result.get('values', [])
        result = service.spreadsheets().values().get(
        spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()
        rows = result.get('values', [])
        

        incsdic = {rows[1][2]: rows[0][2], rows[1][3]: rows[0][3], rows[1][4]: rows[0][4], rows[1][5]:rows[0][5], rows[1][6]:rows[0][6]}
        
        print(incsdic['kram'])
        
        #for row in values:
        #print(row[0], row[1], row[2], row[3], row[4], row[5], row[6])

    except HttpError as err:
        print(err)


bot = telebot.TeleBot('5454592147:AAH0moBxHVVM45CcEarkQjGKT4Wg5J7j0RI')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, <b>{message.from_user.first_name}!</b> Впиши, пожалуйста, свой ник', parse_mode='html')
    nick = message.text

@bot.message_handler()
def get_user(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("kram")
    btn2 = types.KeyboardButton("ivy")
    btn3 = types.KeyboardButton("frida")
    btn4 = types.KeyboardButton("kektor")
    btn5 = types.KeyboardButton("hope")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    
    
    try:
        if(message.text.lower() == "kram"):
            bot.send_message(message.chat.id, text= f"Ты дежуришь в {Sheets.incsdic['kram']}")
        elif(message.text.lower() == "ivy"):
            bot.send_message(message.chat.id, text= f"Ты дежуришь в {Sheets.incsdic['ivy']}")
        elif(message.text.lower() == "frida"):
            bot.send_message(message.chat.id, text= f"Ты дежуришь в {Sheets.incsdic['frida']}")
        elif(message.text.lower() == "kektor"):
            bot.send_message(message.chat.id, text= f"Ты дежуришь в {Sheets.incsdic['kektor']}")
        elif(message.text.lower() == "hope"):
            bot.send_message(message.chat.id, text= f"Ты дежуришь в {Sheets.incsdic['hope']}")
        elif(message.text.lower() == "ayran"):
            bot.send_message(message.chat.id, text= f"Ты дежуришь в {Sheets.incsdic['ayran']}")
        elif(message.text.lower() == "toen"):
            bot.send_message(message.chat.id, text= f"Ты дежуришь в {Sheets.incsdic['toen']}")
        elif(message.text.lower() == "ruth"):
            bot.send_message(message.chat.id, text= f"Ты дежуришь в {Sheets.incsdic['ruth']}")
        elif(message.text.lower() == "daya"):
            bot.send_message(message.chat.id, text= f"Ты дежуришь в {Sheets.incsdic['daya']}")
        elif(message.text.lower() == "wonder"):
            bot.send_message(message.chat.id, text= f"Ты дежуришь в {Sheets.incsdic['wonder']}")
        else:
            bot.send_message(message.chat.id, text= f"Кажется, ты не работаешь в русапорте:(")
    
    except KeyError:
        bot.send_message(message.chat.id, text= f"На этой неделе ты не дежуришь") 
    
    


bot.polling(non_stop=True)



