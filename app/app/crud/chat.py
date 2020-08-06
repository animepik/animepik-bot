from app.models import Chat


class CRUDChat:
    @staticmethod
    async def get(chat_id: int) -> Chat:
        return await Chat.query.where(Chat.id == chat_id).gino.first()

    @staticmethod
    async def update(chat_obj: Chat, **kwargs) -> Chat:
        return await chat_obj.update(**kwargs).apply()

    @staticmethod
    async def create(chat_id: int) -> Chat:
        return await Chat(id=chat_id).create()

    async def get_or_create(self, chat_id: int) -> Chat:
        return await self.get(chat_id) or await self.create(chat_id)
