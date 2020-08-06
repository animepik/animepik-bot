from app.models import ChatMember


class CRUDChatMember:
    @staticmethod
    async def get(chat_id: int, user_id: int) -> ChatMember:
        return await ChatMember.query.where(ChatMember.chat_id == chat_id, ChatMember.user_id == user_id).gino.first()

    @staticmethod
    async def update(user_obj: ChatMember, **kwargs) -> ChatMember:
        return await user_obj.update(**kwargs).apply()

    @staticmethod
    async def create(chat_id: int, user_id: int) -> ChatMember:
        return await ChatMember(chat_id=chat_id, user_id=user_id).create()

    async def get_or_create(self, chat_id: int, user_id: int) -> ChatMember:
        return await self.get(chat_id, user_id) or await self.create(chat_id, user_id)
