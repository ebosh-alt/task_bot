from aiogram import types, Router
from aiogram.filters import CommandStart
from aiogram.methods import SendMessage
from aiogram.types import Message
from bot import keyboards as kb
from bot.config import link_to_bot
from bot.db import users, User
from bot.utils import get_mes

router = Router()


