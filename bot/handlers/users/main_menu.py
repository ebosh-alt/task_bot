from aiogram import types, Router
from aiogram.filters import CommandStart
from aiogram.methods import SendMessage
from aiogram.types import Message
from bot import keyboards as kb
from bot.config import link_to_bot
from bot.db import users, User
from bot.utils import get_mes
from bot.states import States
from aiogram.fsm.context import FSMContext

router = Router()


@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    id = message.from_user.id
    user = await users.get_user(id)
    if user:
        mes = await SendMessage(
            chat_id=id,
            text=get_mes("message/main_menu.md"),
            reply_markup=kb.main_menu,
        )
        user.bot_message_id = mes.message_id
    else:
        user = User(id)
        mes = await SendMessage(
            chat_id=id,
            text=get_mes("message/input_fio.md")
        )
        user.bot_message_id = mes.message_id
        await state.set_state(States.input_fio.state)
        users.add(user)
    users.update_info(user)


main_menu = router
