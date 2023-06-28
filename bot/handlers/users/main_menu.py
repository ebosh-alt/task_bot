from aiogram import types, Router
from aiogram.filters import CommandStart
from aiogram.methods import SendMessage
from aiogram.types import Message
from bot import keyboards as kb
from bot.config import link_to_bot
from bot.db import users, User
from bot.utils import get_mes

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    id = message.from_user.id
    user = await users.get_user(id)
    if user:
        mes = await SendMessage(
            chat_id=id,
            text=get_mes("main_menu"),
            reply_markup=kb.main_menu,
        )
        user.bot_message_id = mes.message_id
    else:
        mes = await SendMessage(
            chat_id=id,
            text=get_mes("register"),
            reply_markup=kb.register,
        )
        user.bot_message_id = mes.message_id
    await users.add_user(user)


main_menu = router
