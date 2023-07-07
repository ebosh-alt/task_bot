from aiogram import types, Router
from aiogram.filters import CommandStart
from aiogram.methods import SendMessage, EditMessageText
from aiogram.types import Message, CallbackQuery
from bot import keyboards as kb
from bot.config import link_to_bot
from bot.db import users, User, countries
from bot.utils import get_mes
from bot.states import States
from aiogram.fsm.context import FSMContext

router = Router()


@router.message(States.input_fio)
async def input_fio(message: Message, state: FSMContext):
    id = message.from_user.id
    user = users.get(id)
    data_user = message.text.split(" ")
    if len(data_user) != 3:
        await message.answer(get_mes("message/fio_error.md"))
        return 404
    first_name = data_user[0]
    last_name = data_user[1]
    patronymic = data_user[2]
    user.firstname = first_name
    user.lastname = last_name
    user.patronymic = patronymic
    await EditMessageText(chat_id=id,
                          message_id=user.bot_message_id,
                          text=get_mes("message/input_country.md"),
                          reply_markup=kb.create_reply_keyboard(countries.get_all()))
    await state.set_state(States.input_country)
    users.update(user)


@router.callback_query(States.input_country)
async def input_fio(call: CallbackQuery, state: FSMContext):
    id = call.from_user.id
    user = users.get(id)
    country = call.data
    id_country = countries.get_id(country)
    user.id_country = id_country
    await EditMessageText(chat_id=id,
                          message_id=user.bot_message_id,
                          text=get_mes("message/.md"),
                          reply_markup=)
    users.update(user)
