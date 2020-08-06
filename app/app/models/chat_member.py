from typing import TYPE_CHECKING

from app.core.db import db
from sqlalchemy import Column, BigInteger, ForeignKey, sql
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from .chat import Chat  # noqa
    from .user import User  # noqa


class ChatMember(db.Model):
    __tablename__ = 'chat_member'
    query: sql

    chat = relationship('Chat')
    chat_id = Column(BigInteger, ForeignKey('chat.id'), primary_key=True)

    user = relationship('User')
    user_id = Column(BigInteger, ForeignKey('user.id'), primary_key=True)
