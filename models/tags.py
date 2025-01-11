import uuid

from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db
from models.items_tags_xref import items_tags_xref


class Tags(db.Model):
    __tablename__ = "Tags"

    tag_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tag_name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String())

    items = db.relationship('Items', secondary=items_tags_xref, back_populates='tags')

    def __init__(self, tag_name, description):
        self.tag_name = tag_name
        self.description = description

    def new_tag_obj():
        return Tags("", "", "")
    

class TagsSchema(ma.Schema):
    class Meta:
        fields = ['tag_id', 'tag_name', 'description']


tag_schema = TagsSchema()
tags_schema = TagsSchema(many=True)