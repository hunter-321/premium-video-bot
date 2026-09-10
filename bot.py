import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import time

# यहाँ अपना असली टेलीग्राम बॉट टोकन डालें
TOKEN = "8138470570:AAHjPRMQwV3_ZRREIkGQL6gF3RTVlfTr56M"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = (
        "👋 **VIP प्रीमियम वीडियो क्लब में आपका स्वागत है!** ✨\n\n"
        "🔥 यहाँ आपको क्या मिलेगा और यह कैसे काम करता है:\n"
        "1️⃣ **Full Entertainment:** हर दिन सुबह और शाम को मनोरंजन के लिए 2 धमाकेदार प्रीमियम वीडियो आएंगी.\n"
        "2️⃣ **100% Safe & Secure:** आपकी प्राइवेसी हमारी पहली प्राथमिकता है. Telegram Stars पेमेंट पूरी तरह से गुप्त (Anonymous) है.\n"
        "3️⃣ **Exclusive VIP Content:** प्राइवेसी सुरक्षा के कारण इसे गैलरी में सेव, स्क्रीनशॉट या फॉरवर्ड नहीं किया जा सकता.\n\n"
        "⚡ मनोरंजन के लिए नीचे दिए गए दो विकल्पों में से चुनें:\n\n"
        "📺 **विकल्प 1: सिर्फ देखने के लिए (2 Stars)**\n"
        "👉 यह वीडियो सुरक्षा कारणों से 3 दिन (72 घंटे) बाद खुद ब खुद डिलीट हो जाएगी.\n"
        "👉 24 घंटे के बाद वीडियो को दोबारा देखने के लिए 2 Stars फिर से पे करने होंगे.\n\n"
        "📥 **विकल्प 2: हमेशा के लिए डाउनलोड करें (5 Stars)**\n"
        "👉 केवल 5 Stars देकर आप इस वीडियो को सीधे अपने phone की गैलरी में सेव कर सकते हैं!\n\n"
        "💳 **Stars को buy करने का आसान तरीका:**\n"
        "👉 जैसे ही आप नीचे किसी भी बटन पर क्लिक करेंगे, पेमेंट का विकल्प आ जाएगा. आप अपने UPI (PhonePe, Paytm, GooglePay) या Google Play के जरिए तुरंत Stars खरीद सकते हैं."
    )
    
    markup = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton("📺 विकल्प 1: सिर्फ देखें (2 Stars)", callback_data="watch_2_stars")
    btn2 = InlineKeyboardButton("📥 विकल्प 2: डाउनलोड करें (5 Stars)", callback_data="download_5_stars")
    markup.add(btn1, btn2)
    
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode="Markdown")

# 24/7 बिना क्रैश हुए चलाने वाला एरर हैंडलिंग लूप
while True:
    try:
        bot.polling(none_stop=True, interval=2, timeout=60)
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)
