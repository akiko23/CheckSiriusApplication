import time

from aiogram import Bot, Dispatcher, executor, types

from db import Database
from markups import main_keyboard
from parse_sirius import get_data, most_main_check

bot = Bot('5215415202:AAHT-M0Ee1sfvjyhWqAJagNsRH3AwrRvu2k')

dp = Dispatcher(bot=bot)

db = Database(db_file='data.db')


@dp.message_handler(commands=['start'])
async def start(mes: types.Message):
    if mes.from_user.id == 818525681:
        get_data()
        time.sleep(1)

        if most_main_check():
            for i in range(20):
                await bot.send_message(818525681,
                                       'Заявка на сайте!!!!!!!\nhttps://siriuscollege.ru/090207-informatsionnie-sistemi-i-programmirovanie')

        else:
            await bot.send_message(818525681, 'Заявки нет 😔')
    await bot.send_message(mes.from_user.id,
                           'Введите номер снилса (пример: 111-111-511 17)\nСмотреть все заявки: /get_all', reply_markup=main_keyboard)


@dp.message_handler(commands=['get_all'])
async def get_all(mes: types.Message):
    if mes.from_user.id == 818525681:
        get_data()
        time.sleep(1)

        if most_main_check():
            for i in range(20):
                await bot.send_message(818525681,
                                       'Заявка на сайте!!!!!!!\nhttps://siriuscollege.ru/090207-informatsionnie-sistemi-i-programmirovanie')

        else:
            await bot.send_message(818525681, 'Заявки нет 😔')

    all_data_list = [element for element in get_data()]

    for el in all_data_list:
        await bot.send_message(mes.from_user.id,
                               f"Номер заявки: {el['count']}\nСНИЛС: {el['snils']}\nБаллы: {el['balls']}")


@dp.message_handler(content_types=['text'])
async def get_number(mes: types.Message):
    if mes.from_user.id == 818525681:
        get_data()
        time.sleep(1)

        if most_main_check():
            for i in range(20):
                await bot.send_message(818525681,
                                       'Заявка на сайте!!!!!!!\nhttps://siriuscollege.ru/090207-informatsionnie-sistemi-i-programmirovanie')

        else:
            await bot.send_message(818525681, 'Заявки нет 😔')

    if mes.text == 'Все_Заявки':
        all_data_list = [element for element in get_data()]

        for el in all_data_list:
            await bot.send_message(mes.from_user.id,
                                   f"Номер заявки: {el['count']}\nСНИЛС: {el['snils']}\nБаллы: {el['balls']}")

    elif mes.text == 'Обновить_базу':
        await bot.send_message(mes.chat.id, 'Обновляю...')

        db.set_current_len(18)

        get_data()
        await bot.delete_message(mes.chat.id, mes.message_id + 1)

        await mes.answer('Обновление завершено✅')

        new_len = len(get_data())

        if new_len > db.get_current_len():
            await bot.send_message(mes.from_user.id, f'Есть изменения. Было добавлено {new_len - db.get_current_len()} новых заявок')
            db.delete_current_len(db.get_current_len())

            db.set_current_len(new_len)
        else:
            db.delete_current_len(db.get_current_len())
            await bot.send_message(mes.from_user.id, 'Изменений нет')
    else:

        try:
            number = db.get_data_with_snils(mes.text)[0]
            grade = db.get_data_with_snils(mes.text)[1]

            if number or grade is not None:
                await mes.answer(
                    f'Ваша заявка есть на сайте!\nНомер: {number}\nОбщий балл: {grade}\nПодробнее тут: https://siriuscollege.ru/090207-informatsionnie-sistemi-i-programmirovanie')

        except IndexError:
            await bot.send_message(mes.from_user.id, 'Такой заявки нет на сайте')


if __name__ == '__main__':
    executor.start_polling(dp)
