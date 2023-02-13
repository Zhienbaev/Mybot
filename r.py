import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, Update

# создание бота с токеном
bot = telebot.TeleBot("5463072483:AAHgKxP2KUZLRh-p2-FE4HUguEKwdtwleGg")

# создание клавиатуры
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(
    KeyboardButton("Отправить сообщение"),
    KeyboardButton("Принять заказ"),
    KeyboardButton("Ссылки"),
    KeyboardButton("Выйти")
)

# обработчик команды /start
@bot.message_handler(commands=["start"])
def start_handler(message: Update):
    # получение имени пользователя
    user_name = message.from_user.first_name
    # отправка приветственного сообщения и клавиатуры
    bot.send_message(
        message.chat.id,
        f"Здравствуйте, {user_name}!",
        reply_markup=keyboard
    )

# обработчик нажатия на кнопку "Отправить сообщение"
@bot.message_handler(func=lambda message: message.text == "Отправить сообщение")
def send_message_handler(message: Update):
    # отправка сообщения автору бота
    bot.send_message(
        "708012523",
        f"Сообщение от {message.from_user.first_name}: {message.text}"
    )

# обработчик нажатия на кнопку "Принять заказ"
@bot.message_handler(func=lambda message: message.text == "Принять заказ")
def accept_order_handler(message: Update):
    # отправка сообщения с инструкцией
    bot.send_message(
        message.chat.id,
        "Напишите свой заказ. Когда закончите, введите команду /заказ"
    )

    # обработчик команды /заказ
    @bot.message_handler(commands=["заказ"])
    def order_handler(message: Update):
        # отправка заказа автору бота
        bot.send_message(
            "708012523",
            f"Заказ от {message.from_user.first_name}: {message.text}"
        )

        # отправка подтверждения клиенту
        bot.reply_to(message, "Заказ принят, ожидайте ответа.")

# обработчик нажатия на кнопку "Ссылки"
@bot.message_handler(func=lambda message: message.text == "Ссылки")
def links_handler(message: Update):
    # отправка пустого сообщения
    bot.send_message(message.chat.id, "Ссылки пока не доступны.")

# обработчик нажатия на кнопку "Выйти"
@bot.message_handler(func=lambda message: message.text == "Выйти")
def exit_handler(message: Update):
    # отправка прощального сообщения и удаление клавиатуры
    bot.send_message(
        message.chat.id,
        "До свидания!",
        reply_markup=ReplyKeyboardMarkup(remove_keyboard=True)
    )

# запуск бота
bot.polling()