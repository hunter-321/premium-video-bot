import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import time
import sys

# 1. आपका बिल्कुल नया टेलीग्राम बॉट टोकन यहाँ सेट कर दिया है
TOKEN = "8674759146:AAGtZFmQvPePvK6JK7oEyXfcpDbdpKQ7y-w"
bot = telebot.TeleBot(TOKEN)

# 2. आपकी असली टेलीग्राम यूजर आईडी (Admin ID)
ADMIN_ID = 8922080909

# वीडियो स्टोर करने के लिए डेटाबेस (शुरुआती सेटअप)
stored_videos = {}

# यह फंक्शन निर्देशों का मैसेज भेजने के लिए है
def send_welcome_logic(chat_id):
    welcome_text = (
        "👋 **VIP प्रीमियम वीडियो क्लब में आपका स्वागत है!** ✨\n\n"
        "🔥 यहाँ आपको क्या मिलेगा और यह कैसे काम करता है:\n"
        "1️⃣ **Full Entertainment:** हर दिन सुबह और शाम को मनोरंजन के लिए 2 धमाकेदार प्रीमियम वीडियो आएंगी.\n"
        "2️⃣ **100% Safe & Secure:** आपकी प्राइवेसी हमारी पहली प्राथमिकता है. Telegram Stars पेमेंट पूरी तरह से गुप्त.\n"
        "3️⃣ **Exclusive VIP Content:** सुरक्षा कारणों से इसे गैलरी में सेव या फॉरवर्ड नहीं किया जा सकता.\n\n"
        "⚡ मनोरंजन के लिए नीचे दिए गए दो विकल्पों में से चुनें:\n\n"
        "📺 **विकल्प 1: सिर्फ देखने के लिए (2 Stars)**\n"
        "📥 **विकल्प 2: हमेशा के लिए डाउनलोड करें (5 Stars)**"
    )
    
    markup = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton("📺 विकल्प 1: सिर्फ देखें (2 Stars)", callback_data="watch_2_stars")
    btn2 = InlineKeyboardButton("📥 विकल्प 2: डाउनलोड करें (5 Stars)", callback_data="download_5_stars")
    markup.add(btn1, btn2)
    
    bot.send_message(chat_id, welcome_text, reply_markup=markup, parse_mode="Markdown")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    send_welcome_logic(message.chat.id)

# जब कोई यूजर इंस्टाग्राम या वेबसाइट के स्पेशल लिंक पर टच करके आएगा
@bot.message_handler(func=lambda message: message.text and message.text.startswith('/start bio'))
def handle_insta_bio(message):
    send_welcome_logic(message.chat.id)

# --- एडमिन पैनल का कोड ---
@bot.message_handler(commands=['panel'])
def admin_panel(message):
    if message.from_user.id == ADMIN_ID:
        panel_text = (
            "⚙️ **VIP बॉट एडमिन पैनल में आपका स्वागत है**\n\n"
            "यहाँ से आप अपने बॉट में प्रीमियम वीडियो अपलोड और मैनेज कर सकते हैं.\n\n"
            "👇 वीडियो सेट करने के लिए नीचे दिए गए बटन का उपयोग करें:"
        )
        markup = InlineKeyboardMarkup()
        btn = InlineKeyboardButton("📤 नई प्रीमियम वीडियो अपलोड करें", callback_data="upload_video_panel")
        markup.add(btn)
        bot.send_message(message.chat.id, panel_text, reply_markup=markup, parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, "❌ क्षमा करें, यह कमांड केवल बॉट के ओनर (Admin) के लिए है.")

# 24/7 बिना क्रैश हुए चलाने वाला सुरक्षित लूप
if __name__ == "__main__":
    while True:
        try:
            bot.polling(none_stop=True, interval=2, timeout=60)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)
