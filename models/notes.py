import uuid
from datetime import datetime, timezone

from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db


class Notes(db.Model):
    __tablename__ = "Notes"

    note_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("AppUsers.user_id"), nullable=False)
    item_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Items.item_id"), nullable=False)
    content = db.Column(db.String(), nullable=False)
    link_url = db.Column(db.String())
    link_type = db.Column(db.String())
    date_time = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.now(timezone.utc))

    user = db.relationship("AppUsers", back_populates="note")
    item = db.relationship("Items", back_populates="notes")

    def __init__(self, user_id, item_id, content, link_url, link_type, date_time):
        self.user_id = user_id
        self.item_id = item_id
        self.content = content
        self.link_url = link_url
        self.link_type = link_type
        self.date_time = date_time


    def new_note_obj():
        return Notes("", "", "", "", "", "")
    

class NotesSchema(ma.Schema):
    class Meta:
        fields = ['note_id', 'content', 'link_url', 'link_type' 'date_time', 'user', 'item']
    user = ma.fields.Nested("AppUsersSchema")
    item = ma.fields.Nested("ItemsSchema")


note_schema = NotesSchema()
notes_schema = NotesSchema(many=True)