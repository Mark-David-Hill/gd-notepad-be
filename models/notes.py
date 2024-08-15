import uuid
from datetime import datetime

from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db


class Notes(db.Model):
    __tablename__ = "Notes"

    note_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("AppUsers.user_id"), nullable=False)
    element_id = db.Column(UUID(as_uuid=True), db.ForeignKey("GameElements.element_id"), nullable=False)
    content = db.Column(db.String(), nullable=False)
    date_time = db.Column(db.DateTime(), nullable=False, default=datetime.now())

    user = db.relationship("AppUsers", back_populates="note")
    element = db.relationship("GameElements", back_populates="note")

    def __init__(self, user_id, content, date_time):
        self.user_id = user_id
        self.content = content
        self.date_time = date_time


    def new_note_obj():
        return Notes("", "", "")
    

class NotesSchema(ma.Schema):
    class Meta:
        fields = ['note_id', 'content', 'date_time', 'user', 'element']
    user = ma.fields.Nested("AppUsersSchema")
    element = ma.fields.Nested("GameElementsSchema")


note_schema = NotesSchema()
notes_schema = NotesSchema(many=True)