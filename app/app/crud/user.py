from app.models import User


class CRUDUser:
    @staticmethod
    async def get(user_id: int) -> User:
        return await User.query.where(User.id == user_id).gino.first()

    @staticmethod
    async def update(user_obj: User, **kwargs) -> User:
        return await user_obj.update(**kwargs).apply()

    @staticmethod
    async def create(user_id: int) -> User:
        return await User(id=user_id).create()

    async def get_or_create(self, user_id: int) -> User:
        return await self.get(user_id) or await self.create(user_id)
