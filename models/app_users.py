import uuid

from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db


class AppUsers(db.Model):
    __tablename__ = "AppUsers"

    user_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    role = db.Column(db.String(), nullable=False, default="user")
    active = db.Column(db.Boolean(), nullable=False, default=True)

    auth = db.relationship("AuthTokens", back_populates="user")

    def __init__(self, first_name, last_name, email, password, role, active):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.role = role
        self.active = active

    def new_user_obj():
        return AppUsers("", "", "", "", "", True)
    

class AppUsersSchema(ma.Schema):
    class Meta:
        fields = ['user_id', 'first_name', 'last_name', 'email', 'role', 'active']


app_user_schema = AppUsersSchema()
app_users_schema = AppUsersSchema(many=True)