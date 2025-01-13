import uuid
from datetime import datetime, timezone

from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db


class AuthTokens(db.Model):
    __tablename__ = "AuthTokens"

    auth_token = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Users.user_id", ondelete="CASCADE"), nullable=False)
    expiration = db.Column(db.DateTime(timezone=True), nullable=False)

    user = db.relationship("Users", back_populates="auth")

    def __init__(self, user_id, expiration):
        self.user_id = user_id
        self.expiration = expiration


class AuthTokensSchema(ma.Schema):
    class Meta:
        fields = ["auth_token", "user_id", "expiration"]


auth_token_schema = AuthTokensSchema()
auth_tokens_schema = AuthTokensSchema(many=True)