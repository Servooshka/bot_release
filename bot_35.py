import telebot
from telebot import types
from telebot.types import Message
import time, random
import datetime

import threading



admin_id = 580051506
users = {}
admins = {}
classes = {}

subjects_5а_class = {}
subjects_5б_class = {}
subjects_6а_class = {}
subjects_6б_class = {}
subjects_7а_class = {}
subjects_7б_class = {}
subjects_8а_class = {}
subjects_8б_class = {}
subjects_9а_class = {}
subjects_9б_class ={}
subjects_10_class = {}
subjects_11_class = {}



TOKEN = '5899008583:AAFKUCDkY-Fn9XheGPwhkWpYlAwPsy7Ase8'



with open("Данные/set_class.txt", "r", encoding = "Windows-1251") as f:
    for line in f:
        user_id_set_class, user_class = line.strip().split(":")
        classes[int(user_id_set_class)] = user_class
    


with open("Данные/users.txt", "r") as f:
    for line in f:
        user, user_id = line.strip().split(":")
        users[user] = int(user_id)


with open("Данные/admins.txt", "r") as f:
    for line in f:
        user, user_id = line.strip().split(":")
        admins[user] = int(user_id)

chtenie_classov = ['5А', '5Б', '6А', '6Б', '7А', '7Б', '8А', '8Б', '9А', '9Б', '10', '11' ]
for i in range(0, 5):
    for n in chtenie_classov:
        with open(f"Данные/subjects_{n}_class/{i}.txt", "r", encoding = "utf-8") as f:
            for line in f:
                nomer, urok_nomer = line.strip().split(":")
                subjects_10_class[nomer] = str(urok_nomer)

# for i in range(0, 5):
#     with open(f"Данные/subjects_9б_class/{i}.txt", "r", encoding = "utf-8") as f:
#         for line in f:
#             nomer, urok_nomer = line.strip().split(":")
#             subjects_10_class[nomer] = str(urok_nomer)

# for i in range(0, 5):
#     with open(f"Данные/subjects_10_class/{i}.txt", "r", encoding = "utf-8") as f:
#         for line in f:
#             nomer, urok_nomer = line.strip().split(":")
#             subjects_10_class[nomer] = str(urok_nomer)

# for i in range(0, 5):
#     with open(f"Данные/subjects_11_class/{i}.txt", "r", encoding = "utf-8") as f:
#         for line in f:
#             nomer, urok_nomer = line.strip().split(":")
#             subjects_11_class[nomer] = str(urok_nomer)



bot = telebot.TeleBot(TOKEN)

now = datetime.datetime.now()
weekday = now.weekday()
current_time = now.time()




hub = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('/start')
# btn2 = types.KeyboardButton("Помощь", request_contact=True)
help_button = types.KeyboardButton("Помощь")
rasp_button = types.KeyboardButton('Расписание')
moe_rasp_button = types.KeyboardButton('Мое расписание')
rasp_na_den_button = types.KeyboardButton('Расписание на сегодня')
moe_raspisanie_na_den_button = types.KeyboardButton('Мое расписание на сегодня')
predl_button = types.KeyboardButton('Есть предложение')
urok_button = types.KeyboardButton('Какой сейчас урок')
urok_u_menya_button = types.KeyboardButton('Какой у меня сейчас урок')
donate_button = types.KeyboardButton('Донат')
school_site_button = types.KeyboardButton('Электронный дневник')

# markup.add(btn1)
# hub.add(school_site_button)

# hub.add(rasp_button, moe_raspisanie_na_den_button)
# hub.add(rasp_na_den_button, urok_button)
# hub.add(school_site_button, help_button, predl_button)

hub.add(moe_rasp_button, rasp_button)
hub.add(moe_raspisanie_na_den_button, rasp_na_den_button)
hub.add(urok_u_menya_button, urok_button)
hub.add(school_site_button, help_button, predl_button)

# hub.add(donate, school_site)
# hub.add(school_site)

rasp = types.ReplyKeyboardMarkup(resize_keyboard=True)
class5 = types.KeyboardButton("5")
class6 = types.KeyboardButton("6")
class7 = types.KeyboardButton("7")
class8 = types.KeyboardButton("8")
class9 = types.KeyboardButton("9")
class10 = types.KeyboardButton("10")
class11 = types.KeyboardButton("11")
back = types.KeyboardButton("Назад")

rasp.add(class5, class6, class7)
rasp.add(class8, class9, class10)
rasp.add(class11)
rasp.add(back)

bukva_classa_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
class_9a = types.KeyboardButton("А")
class_9b = types.KeyboardButton("Б")

bukva_classa_menu.add(class_9a, class_9b)

back_button = types.ReplyKeyboardMarkup(resize_keyboard=True)
back_button.add(back)


confirm_or_reject = types.ReplyKeyboardMarkup(resize_keyboard=True)
confirm_button = types.KeyboardButton('Да')
reject_button = types.KeyboardButton('Нет')

confirm_or_reject.add(confirm_button, reject_button)




zvonki = [510, 555, 565, 610, 630, 675, 695, 740, 755, 800, 815, 860, 870, 915, 925, 970, 975, 1020]





code = random.randint(1,10000)
command_confirm = False
command_predl = False
text_predl = "Есть предложение"
text_rasp = "Расписание"
text_back = "Назад"
text_help = "Помощь"
text_help1 = "помощь"
text_urok = "Урок"
isckl = "Есть предложениеРасписаниеНазадПомощьпомощьУрок1234567891011"
classi = "5, 6, 7, 8, 9"
classi_bez_bukv = "10, 11"
bukvi = "А, Б"



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text="Добро пожаловать, {0.first_name}! Я бот, созданный для написания пожеланий по улучшения нашей школы.".format(message.from_user), reply_markup=hub)
    if (message.from_user.id not in users.values()):    
        users[message.from_user.username] = message.from_user.id   
        print(users)
        print(f"Пользователь {message.from_user.username} подписался на бота")
        with open("Данные/users.txt", "w") as f:
            for user, user_id in users.items():
                f.write("{}:{}\n".format(user, user_id))
    


# print(admins)
# print(users)

@bot.message_handler(commands=['send_message'])
def send_message(message: Message):
    if message.from_user.id in admins.values():
        bot.send_message(message.chat.id, "Что отправить?", reply_markup=back_button)
        bot.register_next_step_handler_by_chat_id(message.chat.id, rassilka)
    else:
        bot.send_message(message.chat.id, "Вы не админ")

def rassilka(message: Message):
    global text_rassilka
    text_rassilka = message.text
    print(text_rassilka)
    if text_rassilka == "Назад":
        bot.send_message(message.chat.id, "Что ты хочешь сделать?", reply_markup=hub)
    else:
        bot.reply_to(message, "Подтверждаете рассылку этого сообщения?")
        bot.send_message(message.chat.id, "Нажмите да, если подтверждаете", reply_markup=confirm_or_reject)
        bot.register_next_step_handler_by_chat_id(message.chat.id, rassilka_confirm)


def rassilka_confirm(message:Message):
    global text_rassilka
    if message.text == "Да":
        print(f"РАССЫЛКА ОТ {message.from_user.username}: {text_rassilka}")
        for user_id in users.values():
            try:
                bot.send_message(user_id, text_rassilka)
            except:
                continue
        bot.send_message(message.chat.id, "Рассылка отправлена", reply_markup=hub)
    elif message.text == "Нет":
        bot.send_message(message.chat.id, "Что ты хочешь сделать?", reply_markup=hub)

        
@bot.message_handler(commands=['admin'])
def admin_code(message: Message):
    global user_to_admin, timer, user_to_admin_id, user_to_admin_name

    # code = random.randint(10000, 50000)
    user_to_admin = message.chat.id
    user_to_admin_id = message.from_user.id
    user_to_admin_name = message.from_user.username
    print(user_to_admin_id)
    if user_to_admin_id in admins.values():
        bot.send_message(user_to_admin, "Вы уже админ", reply_markup=hub)
        return
    else:
        bot.send_message(admin_id, "Утвердить запрос?", reply_markup=confirm_or_reject)
        bot.forward_message(admin_id, message.chat.id, message.message_id)
        bot.register_next_step_handler_by_chat_id(admin_id, confirm_by_admin)

        timer = threading.Timer(10.0, hub_keyboard_from_admin_confirm, args=[message])
        timer.start()



def confirm_by_admin(message: Message):
    global user_to_admin, timer

    

    if message.text == "Да":
        bot.send_message(admin_id, "Запрос утвержден", reply_markup=hub)
        # bot.send_message(user_to_admin, "Ваш запрос утвержден, теперь вы админ")
        timer.cancel()
        print(timer)
        confirm_code(message)
    elif message.text == "Нет":
        bot.send_message(user_to_admin, "Запрос отклонен")
        bot.send_message(admin_id, "Запрос отклонен", reply_markup=hub)
        timer.cancel()

        
def hub_keyboard_from_admin_confirm(message):
    global user_to_admin
    bot.send_message(user_to_admin, "Запрос отклонен")
    bot.send_message(admin_id, "Запрос отклонен", reply_markup=hub)



def confirm_code(message):
    global command_confirm, admins, code, user_to_admin, user_to_admin_name, user_to_admin_id
        
    with open("Данные/admins.txt", "w") as f:
        if (user_to_admin_id not in admins.values()):
            admins[user_to_admin_name] = user_to_admin_id
            for user_to_admin_name, user_to_admin_id in admins.items():
                f.write("{}:{}\n".format(user_to_admin_name, user_to_admin_id))
                print(admins)
            bot.send_message(user_to_admin, "Ваш запрос утвержден, теперь вы админ")





@bot.message_handler(func=lambda message: message.text=='Помощь')
def message_helper(message):
    global user_link
    user_id = message.from_user.id
    user_link = f'@{message.from_user.username}'
    
    bot.reply_to(message, "Ждите помощи")
    bot.send_message(admin_id, f"Пользователю {user_link} нужна помощь")
    print(f"Пользователю {user_link} нужна помощь")





@bot.message_handler(func=lambda message: message.text=='Расписание')
def raspisanie(message: Message):
    bot.send_message(message.chat.id, "В каком ты классе?".format(message.from_user), reply_markup=rasp)
    bot.register_next_step_handler_by_chat_id(message.chat.id, vibor_classa)

@bot.message_handler(func=lambda message: message.text=='Мое расписание')
def moe_raspisanie(message):
    set_class_raspisanie(message)
    if set_class_flag == True:
        vibor_classa_moy(message)

def vibor_classa_moy(message:Message):
    bot.send_photo(message.chat.id, open(f'Данные/расписание_{nomer_classa}.jpg', 'rb'), reply_markup=hub)

def vibor_classa(message:Message):
    global class_s_bukvoi
    class_s_bukvoi = message.text

    if message.text == "9" or message.text == "8" or message.text == "7" or message.text == "6" or message.text == "5":
        bot.send_message(message.chat.id, "Какая буква?", reply_markup=bukva_classa_menu)
        bot.register_next_step_handler_by_chat_id(message.chat.id, vibor_bukvi)

        
    elif message.text == "10" or message.text == "11":
        bot.send_photo(message.chat.id, open(f'Данные/расписание_{message.text}.jpg', 'rb'), reply_markup=hub)

    elif message.text == "Назад":

        bot.send_message(message.chat.id, "Что ты хочешь сделать?", reply_markup=hub)

    elif message.text not in classi:
        bot.send_message(message.chat.id, "Неверный класс, выберите из списка")
        bot.register_next_step_handler_by_chat_id(message.chat.id, vibor_classa)

            
def vibor_bukvi(message:Message):
    global class_s_bukvoi
    class_s_bukvoi = class_s_bukvoi + message.text
    bot.send_photo(message.chat.id, open(f'Данные/расписание_{class_s_bukvoi}.jpg', 'rb'), reply_markup=hub)

@bot.message_handler(func=lambda message: message.text=='Какой сейчас урок')
def kakoi_urok(message):
    chistoe_vremya(message)
    # vremya(message)
    # urok = 5
    proverka_dnya_nedeli(message)
    if proverka_dnya_nedeli_flag == True:
        if urok < 100:
            bot.send_message(message.chat.id, "В каком ты классе?", reply_markup=rasp)
            bot.register_next_step_handler_by_chat_id(message.chat.id, vibor_classa_dlya_uroka)
        elif urok == 100:
            bot.send_message(message.chat.id, "Уроки еще не начались")
        elif urok == 101:
            bot.send_message(message.chat.id, "Уроки закончились")

def vibor_classa_kakoi_urok(message:Message):
    global weekday, proverka_dnya_nedeli_flag, class_s_bukvoi
    class_s_bukvoi = message.text
    if message.text == "9" or message.text == "8" or message.text == "7" or message.text == "6" or message.text == "5":
        bot.send_message(message.chat.id, "Какая буква?", reply_markup=bukva_classa_menu)
        bot.register_next_step_handler_by_chat_id(message.chat.id, vibor_bukvi_kakoi_urok)



@bot.message_handler(func=lambda message: message.text=='Какой у меня сейчас урок')
def kakoi_u_menya_urok(message):
    global set_class_flag
    set_class_raspisanie(message)
    chistoe_vremya(message)
    # vremya(message)
    # urok = 5
    if set_class_flag == True and urok < 100:
        vibor_classa_dlya_moego_uroka(message)
    elif set_class_flag == True and urok == 100:
        bot.send_message(message.chat.id, "Уроки еще не начались")
    elif set_class_flag == True and urok == 101:
        bot.send_message(message.chat.id, "Уроки закончились")



def vibor_classa_dlya_uroka(message:Message):
    global nomer_classa_kakoi_urok
    nomer_classa_kakoi_urok = message.text
    if nomer_classa_kakoi_urok == "10" or nomer_classa_kakoi_urok == "11":
        cho_za_urok(message)

    elif nomer_classa_kakoi_urok == "9" or nomer_classa_kakoi_urok == "8" or nomer_classa_kakoi_urok == "7" or nomer_classa_kakoi_urok == "6" or nomer_classa_kakoi_urok == "5":
        bot.send_message(message.chat.id, "Какая буква?", reply_markup=bukva_classa_menu)
        bot.register_next_step_handler_by_chat_id(message.chat.id, vibor_bukvi_kakoi_urok)
    elif message.text == "Назад":
        bot.send_message(message.chat.id, "Что ты хочешь сделать?", reply_markup=hub)
    else:
        bot.send_message(message.chat.id, "Неверный класс, выберите из списка")
        bot.register_next_step_handler_by_chat_id(message.chat.id, vibor_classa_dlya_uroka)

def vibor_bukvi_kakoi_urok(message:Message):
    global class_s_bukvoi, weekday, nomer_classa_kakoi_urok
    nomer_classa_kakoi_urok = nomer_classa_kakoi_urok + message.text
    cho_za_urok(message)

def vibor_classa_dlya_moego_uroka(message):
    global nomer_classa_kakoi_urok, nomer_classa
    nomer_classa_kakoi_urok = nomer_classa
    print(nomer_classa)
    # if nomer_classa == "10" or nomer_classa == "11":
    #     cho_za_urok(message)


        # bot.send_message(message.chat.id, "Какая буква?", reply_markup=bukva_classa_menu)
        # bot.register_next_step_handler_by_chat_id(message.chat.id, vibor_bukvi_moy_urok)

    if message.text == "Назад":
        bot.send_message(message.chat.id, "Что ты хочешь сделать?", reply_markup=hub)
    
    else: # nomer_classa_kakoi_urok == "9" or nomer_classa_kakoi_urok == "8" or nomer_classa_kakoi_urok == "7" or nomer_classa_kakoi_urok == "6" or nomer_classa_kakoi_urok == "5":
        cho_za_urok(message)

    # else:
    #     bot.send_message(message.chat.id, "Неверный класс, выберите из списка")
    #     bot.register_next_step_handler_by_chat_id(message.chat.id, vibor_classa_dlya_moego_uroka)

# lesson_chist = ""

def cho_za_urok(message):
    global urok, weekday, lesson_chist, nomer_classa_kakoi_urok
    proverka_dnya_nedeli(message)
    set_class_raspisanie(message)
    # if set_class_flag == True:
    if proverka_dnya_nedeli_flag == True:
        with open(f"Данные/subjects_{nomer_classa_kakoi_urok}_class/{weekday}.txt", "r", encoding = "utf-8") as f:
            for line in f:
                # print(line)
                lesson = line.strip().split(":")
                # print(lesson)
                
                if lesson[0] == str(urok):
                    lesson_chist = line.strip().split(":")[1]
                    # print(lesson_chist)
                    if urok % 2 != 0:
                        bot.send_message(message.chat.id, f"Сейчас: {lesson_chist} \n\n{vremya(message)}", reply_markup=hub)
                    if urok % 2 == 0:
                        bot.send_message(message.chat.id, f"{lesson_chist}", reply_markup=hub)
    # else:




def vibor_bukvi_moy_urok(message:Message):
    global class_s_bukvoi, weekday, nomer_classa_kakoi_urok
    cho_za_urok(message)

# def cho_za_urok_11_class(message):
#     global urok, weekday, lesson_chist

#     with open(f"Данные/subjects_11_class/{weekday}.txt", "r", encoding = "utf-8") as f:
#         for line in f:

#             lesson = line.strip().split(":")

            
#             if lesson[0] == str(urok):
#                 lesson_chist = line.strip().split(":")[1]

#                 if urok % 2 != 0:
#                     bot.send_message(message.chat.id, f"Сейчас: {lesson_chist}", reply_markup=hub)
#                 if urok % 2 == 0:
#                     bot.send_message(message.chat.id, f"{lesson_chist}", reply_markup=hub)



@bot.message_handler(commands=['set_class'])
def set_class(message: Message):
    global user_id_set_class
    user_id_set_class = message.from_user.id
    # print(user_id_set_class)

    bot.send_message(message.chat.id, "В каком ты классе?", reply_markup=rasp)
    bot.register_next_step_handler_by_chat_id(message.chat.id, vibor_set_class)

def vibor_set_class(message: Message):
    global user_class, user, user_id_set_class
    user_class = message.text
    # user = message.from_user.id
    if message.text in classi:
        bot.send_message(message.chat.id, "Какая буква?", reply_markup=bukva_classa_menu)
        bot.register_next_step_handler_by_chat_id(message.chat.id, kakaya_bukva)

    elif message.text in classi_bez_bukv:
        set_class_bez_bukv(message)

    elif message.text == "Назад":
        bot.send_message(message.chat.id, "Что ты хочешь сделать?", reply_markup=hub)
    
    else:
        bot.send_message(message.chat.id, "Неверный класс")
        bot.register_next_step_handler_by_chat_id(message.chat.id, vibor_set_class)

def set_class_bez_bukv(message):
    global user_id_set_class, user_class
    with open("Данные/set_class.txt", "w") as f:
        if (user_id_set_class not in classes.keys()):
            classes[user_id_set_class] = user_class
            for user_id_set_class, user_class in classes.items():
                f.write("{}:{}\n".format(user_id_set_class, user_class))
            print(classes)
        elif classes[user_id_set_class] != user_class:
            classes[user_id_set_class] = user_class
            for user_id_set_class, user_class in classes.items():
                f.write("{}:{}\n".format(user_id_set_class, user_class))
            print(classes)
        bot.send_message(message.chat.id, "Класс установлен", reply_markup=hub)
    
def set_class_s_bukvami(message):
    global user, bukva_classa, user_class, user_id_set_class
    user_class = user_class + bukva_classa
    # print(user_class)
    # user = message.from_user.id
    # print(user)
    # print(message.from_user.id)

    with open("Данные/set_class.txt", "w") as f:
        if (user_id_set_class not in classes.keys()):
            classes[user_id_set_class] = user_class
            for user_id_set_class, user_class in classes.items():
                f.write("{}:{}\n".format(user_id_set_class, user_class))
            print(classes)
        elif classes[user_id_set_class] != user_class:
            classes[user_id_set_class] = user_class
            for user_id_set_class, user_class in classes.items():
                f.write("{}:{}\n".format(user_id_set_class, user_class))
            print(classes)
        bot.send_message(message.chat.id, "Класс установлен", reply_markup=hub)

def kakaya_bukva(message:Message):
    global bukva_classa, user_id_set_class
    bukva_classa = message.text
    print(bukva_classa)
    print(message.text)
    if bukva_classa in bukvi:
        set_class_s_bukvami(message)


@bot.message_handler(func=lambda message: message.text=='Мое расписание на сегодня')
def set_class_raspisanie_na_den(message):
    set_class_raspisanie(message)
    if set_class_flag == True:
        uroki_na_moy_den(message)
        


@bot.message_handler(func=lambda message: message.text=='Расписание на сегодня')
def raspisanie(message: Message):
    bot.send_message(message.chat.id, "В каком ты классе?".format(message.from_user), reply_markup=rasp)
    bot.register_next_step_handler_by_chat_id(message.chat.id, vibor_classa_rasp_na_den)


def vibor_classa_rasp_na_den(message:Message):
    global weekday, proverka_dnya_nedeli_flag, class_s_bukvoi
    class_s_bukvoi = message.text
    if message.text == "9" or message.text == "8" or message.text == "7" or message.text == "6" or message.text == "5":
        bot.send_message(message.chat.id, "Какая буква?", reply_markup=bukva_classa_menu)
        bot.register_next_step_handler_by_chat_id(message.chat.id, vibor_bukvi_rasp_na_den)


    elif message.text == "10" or message.text == "11":
        
        proverka_dnya_nedeli(message)
        if proverka_dnya_nedeli_flag == True:
            uroki_na_den(message)

    # elif message.text == "11":
    #     uroki_na_den_11_class(message)
            
            
    elif message.text == "Назад":

        bot.send_message(message.chat.id, "Что ты хочешь сделать?", reply_markup=hub)

    else:
        bot.send_message(message.chat.id, "Неверный класс, выберите из списка")
        bot.register_next_step_handler_by_chat_id(message.chat.id, vibor_classa_rasp_na_den)



def vibor_bukvi_rasp_na_den(message:Message):
    global class_s_bukvoi, weekday
    
    class_s_bukvoi = class_s_bukvoi + message.text
    uroki_na_den(message)


def  proverka_dnya_nedeli(message):
    global weekday, proverka_dnya_nedeli_flag
    if weekday < 5:
        proverka_dnya_nedeli_flag = True
    else:
        proverka_dnya_nedeli_flag = False
        bot.send_message(message.chat.id, "Сейчас выходные", reply_markup=hub)



def uroki_na_den(message):
    global weekday, proverka_dnya_nedeli_flag
    proverka_dnya_nedeli(message)
    if proverka_dnya_nedeli_flag == True:
        with open(f"Данные/subjects_{class_s_bukvoi}_class/{weekday}.txt", "r", encoding = "utf-8") as f:
            lessons = ""
            num_uroka = 1
            for line in f:
                # for i in len(f - 1):
                lessons_num = line.strip().split(":")[0]
                lessons_nichego = line.strip().split(":")[1]
                if int(lessons_num) % 2 != 0 and lessons_nichego != "Уроков нет":
                    lessons_chist = line.strip().split(":")[1]
                    lessons += f"{num_uroka}: {lessons_chist}\n"
                    num_uroka += 1
                    # print(lessons)
        bot.send_message(message.chat.id, lessons, reply_markup=hub)

def uroki_na_moy_den(message):
    global weekday, proverka_dnya_nedeli_flag
    proverka_dnya_nedeli(message)
    if proverka_dnya_nedeli_flag == True:
        with open(f"Данные/subjects_{nomer_classa}_class/{weekday}.txt", "r", encoding = "utf-8") as f:
            lessons = ""
            num_uroka = 1
            for line in f:
                # for i in len(f - 1):
                lessons_num = line.strip().split(":")[0]
                lessons_nichego = line.strip().split(":")[1]
                if int(lessons_num) % 2 != 0 and lessons_nichego != "Уроков нет":
                    lessons_chist = line.strip().split(":")[1]
                    lessons += f"{num_uroka}: {lessons_chist}\n"
                    num_uroka += 1
                    # print(lessons)
        bot.send_message(message.chat.id, lessons, reply_markup=hub)

@bot.message_handler(func=lambda message: message.text=='Есть предложение')
def est_predl(message: Message):
    bot.send_message(message.chat.id, "Напиши, что тебе хотелось бы увидеть в этом боте или в школе.", reply_markup=back_button)
    bot.register_next_step_handler(message, napisal_predl)



def napisal_predl(message: Message):
    if message.text == "Назад":
        bot.send_message(message.chat.id, "Что ты хочешь сделать?",  reply_markup=hub)
    else:
        bot.send_message(message.chat.id, "Спасибо за предложение, постараемся учесть его!", reply_markup=hub)
        bot.send_message(admin_id, f"Предложение от пользователся @{message.from_user.username}")
        bot.forward_message(admin_id, message.chat.id, message.message_id)
        # command_predl = False
        print(message.from_user.username, ": ", message.text, sep="")  




@bot.message_handler(func=lambda message: message.text=='Донат')
def send_donate(message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    donate_button = types.InlineKeyboardButton(text="Донат на развитие бота", url="https://www.donationalerts.com/r/servoo")
    keyboard.add(donate_button)
    bot.send_message(chat_id=message.chat.id, text="Нажми, что перейти на страницу доната:", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text=='Электронный дневник')
def send_school_site(message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    school_site_button = types.InlineKeyboardButton(text="Перейти в дневник", url="http://ns35.алмазинка.рф:86")
    keyboard.add(school_site_button)
    bot.send_message(chat_id=message.chat.id, text="Нажми, чтобы перейти в дневник:", reply_markup=keyboard)




@bot.message_handler(content_types=['text'])
def message(message):
    bot.send_message(message.chat.id, "Прости, я тебя не понял")



def set_class_raspisanie(message):
    global classes, nomer_classa, set_class_flag
    proverka_set_class = True
    for user_id in classes:
        if message.from_user.id == user_id:
            nomer_classa = classes[user_id]
            set_class_flag = True
            proverka_set_class = False
            break
    if proverka_set_class == True:

        bot.send_message(message.chat.id, "Я не знаю твой класс. Чтобы его выбрать, нажми /set_class")
        set_class_flag = False



def chistoe_vremya(message):
    global urok, zvonok, result, weekday

    now = datetime.datetime.now()
    weekday = now.weekday()
    current_time = now.time()

    time1 = str(current_time)
    Time = time1[:5].split(":")
    result = int(Time[0]) * 60 + int(Time[1])

    current_time = now.time()
    vremya_zvonka()



def vremya(message):

    global urok, zvonok, result, weekday
    
    now = datetime.datetime.now()
    weekday = now.weekday()
    current_time = now.time()

    time1 = str(current_time)
    Time = time1[:5].split(":")
    result = int(Time[0]) * 60 + int(Time[1])

    current_time = now.time()
    vremya_zvonka()

    if weekday >= 5:
        print("Сейчас выходные")
        return f"Сейчас выходные \n{vremya_zvonka()}"
        bot.send_message(message.chat.id, f"Сейчас выходные \n{vremya_zvonka()}")
        # bot.send_message(message.chat.id, "It's weekend, {}".format(str(vremya_zvonka(message))))

    elif urok == 101:
        print("Уроки закончились")
        return f"Уроки закончились"
        bot.send_message(message.chat.id, f"Уроки закончились")
        return
    elif urok == 100:
        print("Уроки еще не начались")
        return f"Уроки еще не начались"
        bot.send_message(message.chat.id, f"Уроки еще не начались")
        return
    elif urok == 1:
        print("1 урок")
        return f"Сейчас 1 урок. \n{vremya_zvonka()}"
        bot.send_message(message.chat.id, f"Сейчас 1 урок. \n{vremya_zvonka()}")
    # elif urok == 1:
    #     print("Перемена 1")
    elif urok == 2:
        print("Перемена 1")
        return f"Сейчас перемена, следующий урок: 2 \n{vremya_zvonka()}"
        bot.send_message(message.chat.id, f"Сейчас перемена, следующий урок: 2 \n{vremya_zvonka()}")
    elif urok == 3:
        print("2 урок")
        return f"Сейчас 2 урок \n{vremya_zvonka()}"
        bot.send_message(message.chat.id, f"Сейчас 2 урок \n{vremya_zvonka()}")
    elif urok == 4:
        print("Перемена 2")
        return f"Сейчас перемена, следующий урок: 3 \n{vremya_zvonka()}"
        bot.send_message(message.chat.id, f"Сейчас перемена, следующий урок: 3 \n{vremya_zvonka()}")
    elif urok == 5:
        print("3 урок")
        bot.send_message(message.chat.id, f"Сейчас 3 урок \n{vremya_zvonka()}")
    elif urok == 6:
        print("Перемена 3")
        bot.send_message(message.chat.id, f"Сейчас перемена, следующий урок: 4 \n{vremya_zvonka()}")
    elif urok == 7:
        print("4 урок")
        bot.send_message(message.chat.id, f"Сейчас 4 урок \n{vremya_zvonka()}")
    elif urok == 8:
        print("Перемена 4")
        bot.send_message(message.chat.id, f"Сейчас перемена, следующий урок: 5 \n{vremya_zvonka()}")
    elif urok == 9:
        print("5 урок")
        bot.send_message(message.chat.id, f"Сейчас 5 урок \n{vremya_zvonka()}")
    elif urok == 10:
        print("Перемена 5")
        bot.send_message(message.chat.id, f"Сейчас перемена, следующий урок: 6 \n{vremya_zvonka()}")
    elif urok == 11:
        print("6 урок")
        bot.send_message(message.chat.id, f"Сейчас 6 урок \n{vremya_zvonka()}")
    elif urok == 12:
        print("Перемена 6")
        bot.send_message(message.chat.id, f"Сейчас перемена, следующий урок: 7 \n{vremya_zvonka()}")
    elif urok == 13:
        print("7 урок")
        return f"7 урок \n{vremya_zvonka()}"
        bot.send_message(message.chat.id, f"Сейчас 7 урок \n{vremya_zvonka()}")
    elif urok == 14:
        print("Перемена 7")
        bot.send_message(message.chat.id, f"Сейчас перемена, следующий урок: 8 \n{vremya_zvonka()}")
    elif urok == 15:
        print("8 урок")
        bot.send_message(message.chat.id, f"Сейчас 8 урок \n{vremya_zvonka()}")
    elif urok == 16:
        print("Перемена 8")
        bot.send_message(message.chat.id, f"Сейчас перемена, следующий урок: 9 \n {vremya_zvonka()}")
    elif urok == 17:
        print("9 урок")
        bot.send_message(message.chat.id, f"Сейчас 9 урок \n {vremya_zvonka()}")






def vremya_zvonka():
    global zvonok, urok, result, zvonki
    for i in range(18):
        zvonok = zvonki[i] - result
        if zvonok > 0:
            urok = i
            break
            
    if zvonok == 1 or zvonok == 21 or zvonok == 31 or zvonok == 41:
        # return bot.send_message(message.chat.id, f'До звонка осталось {zvonok} минута')
        return f'До звонка осталось {zvonok} минута'
    elif zvonok > 1 and zvonok <= 4 or (zvonok >= 22 and zvonok <= 24) or (zvonok >= 32 and zvonok <= 34) or (zvonok >= 41 and zvonok <= 44):
        # return bot.send_message(message.chat.id, f'До звонка осталось {zvonok} минуты')
        return f'До звонка осталось {zvonok} минуты'
    elif zvonok > 4 and zvonok <= 20 or (zvonok >= 25 and zvonok <= 30) or (zvonok >= 35 and zvonok <= 40) or zvonok == 45:
        # return bot.send_message(message.chat.id, f'До звонка осталось {zvonok} минут')
        return f'До звонка осталось {zvonok} минут'
    elif result > zvonki[-1]:
        urok = 101
        # return bot.send_message(message.chat.id, 'Уроки закончились')
        return 'Уроки закончились'
    elif result < zvonki[0]:
        urok = 100
        # return bot.send_message(message.chat.id, "Уроки еще не начались")
        return "Уроки еще не начались"

try:
    bot.polling(none_stop=True)
except Exception as e:
    print(e)


