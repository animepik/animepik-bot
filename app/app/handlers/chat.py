from aiogram.types import ContentTypes, Message, ParseMode, CallbackQuery
from app.core.bot import dp
from app.keyboards import welcome_keyboard
from app.utils import safe_replace, mention_his, menu, mute, unmute, user_id_from_menu


@dp.message_handler(content_types=ContentTypes.NEW_CHAT_MEMBERS)
async def welcome_new_member(message: Message):
    for user in message.new_chat_members:
        if user.is_bot:
            continue

        mention = await mention_his(user)
        text = await safe_replace('Добро пожаловать, $user!', user=mention)
        keyboard = await welcome_keyboard(user.id)

        await message.answer(text, parse_mode=ParseMode.MARKDOWN, reply_markup=keyboard)
        await mute(message.chat.id, user, silent=True)


@dp.callback_query_handler(menu('spam_protect', 0))
async def spam_protect(callback_query: CallbackQuery):
    user_id = await user_id_from_menu(callback_query.data, 1)

    if user_id is None:
        return

    if callback_query.from_user.id != user_id:
        await callback_query.answer('Только для нового пользователя!')
        return

    success = await unmute(callback_query.message.chat.id, callback_query.from_user, silent=True)

    if success:
        keyboard = await welcome_keyboard()
        await callback_query.message.edit_reply_markup(keyboard)

    await callback_query.answer('Приятного общения!' if success else 'Произошла ошибка')
