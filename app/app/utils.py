import re

from aiogram.types import User


async def safe_replace(string, **kwargs: str):
    for old, new in kwargs.items():
        string = re.sub(f'\\${old}', new, string)
    return string


async def mention_user(name: str, user_id: int) -> str:
    return f"[{name}](tg://user?id={user_id})"


async def mention_his(user: User) -> str:
    return await mention_user(user.full_name, user.id)
