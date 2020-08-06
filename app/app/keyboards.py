from typing import Optional

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def welcome_keyboard(check_user: Optional[int] = None) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    if check_user is not None:
        keyboard.add(InlineKeyboardButton('Начать общаться', callback_data=f'spam_protect/{check_user}'))

    return keyboard
