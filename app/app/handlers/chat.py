from aiogram.types import ContentTypes, Message, ParseMode
from app.core.bot import dp
from app.utils import safe_replace, mention_his


@dp.message_handler(content_types=ContentTypes.NEW_CHAT_MEMBERS)
async def welcome_new_member(message: Message):
    for user in message.new_chat_members:
        if user.is_bot:
            continue

        mention = await mention_his(user)
        text = await safe_replace('Добро пожаловать, $user!', user=mention)
        await message.answer(text, parse_mode=ParseMode.MARKDOWN)
