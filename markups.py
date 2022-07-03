from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
get_all_data = KeyboardButton(text='Все_Заявки')
update_db = KeyboardButton(text='Обновить_базу')

main_keyboard.add(get_all_data)
main_keyboard.add(update_db)

