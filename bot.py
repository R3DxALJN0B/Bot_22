
import telebot
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

TOKEN = "7789954056:AAHolpwolU7T2DiYwgwV6oelbqTnH2cZTrA"
bot = telebot.TeleBot(TOKEN)

ua = UserAgent()

def search_dehashed(query):
    url = f"https://www.dehashed.com/search?query={query}"
    headers = {"User-Agent": ua.random}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    # استخراج بعض المعلومات (مثال)
    return soup.find_all('div', class_='search-result')

def search_hibp(query):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{query}"
    headers = {
        "User-Agent": ua.random,
        "hibp-api-key": "your_api_key_here"  # تحتاج مفتاح API من HIBP
    }
    response = requests.get(url, headers=headers)
    return response.json()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحبًا! أرسل لي اسم المستخدم أو البريد الإلكتروني أو الرقم للبحث.")

@bot.message_handler(func=lambda message: True)
def search_info(message):
    query = message.text
    # البحث في Dehashed أو أي مصدر آخر
    results = search_dehashed(query)
    if results:
        bot.reply_to(message, f"تم العثور على نتائج: {results}")
    else:
        bot.reply_to(message, "لم يتم العثور على نتائج.")
        
bot.polling()
