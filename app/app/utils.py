import re
from datetime import datetime
from typing import List, Union, Optional

from aiogram.types import User, CallbackQuery, ChatPermissions, ParseMode
from aiogram.utils import exceptions
from app.core.bot import bot


async def safe_replace(string, **kwargs: str):
    for old, new in kwargs.items():
        string = re.sub(f'\\${old}', new, string)
    return string


async def mention_user(name: str, user_id: int) -> str:
    return f"[{name}](tg://user?id={user_id})"


async def mention_his(user: User) -> str:
    return await mention_user(user.full_name, user.id)


async def menu_parser(cb_data: str) -> List[Union[str, int]]:
    parsed_menu = cb_data.split('/')
    return [int(line) if line.isdigit() else line for line in parsed_menu]


def menu(value: str, position: int):
    async def wrapper(callback_query: CallbackQuery):
        parsed_menu = await menu_parser(callback_query.data)
        return parsed_menu[position] == value

    return wrapper


async def user_id_from_menu(cb_data: str, position: int) -> Optional[int]:
    parsed_menu = await menu_parser(cb_data)

    try:
        user_id = parsed_menu.pop(position)
        assert user_id is not None
        assert isinstance(user_id, int)
    except AssertionError:
        return
    else:
        return user_id


async def change_permission(
        chat_id: int,
        user_id: int,
        permissions: ChatPermissions,
        until_date: Optional[datetime] = None
) -> bool:
    try:
        await bot.restrict_chat_member(chat_id, user_id, permissions, until_date)
    except exceptions.NotEnoughRightsToRestrict:
        await bot.send_message(chat_id, 'У меня нет прав на измененее разрешений для участников чата!')
        return False
    else:
        return True


async def mute(chat_id: int, user: User, until_date: datetime = None, silent: bool = False) -> bool:
    permissions = ChatPermissions(*[False for _ in range(5)])
    success = await change_permission(chat_id, user.id, permissions, until_date)

    if success and not silent:
        mention = await mention_his(user)
        text = f'*{mention} заткнут*' if not silent else None
        if until_date is not None:
            text += f' *до* _{until_date}_'

        await bot.send_message(chat_id, text, parse_mode=ParseMode.MARKDOWN)

    return success


async def unmute(chat_id: int, user: User, silent: bool = False) -> bool:
    permissions = ChatPermissions(*[True for _ in range(5)])
    success = await change_permission(chat_id, user.id, permissions)

    if success and not silent:
        mention = await mention_his(user)
        text = f'*{mention} теперь снова может общаться!*' if not silent else None

        await bot.send_message(chat_id, text, parse_mode=ParseMode.MARKDOWN)

    return success
