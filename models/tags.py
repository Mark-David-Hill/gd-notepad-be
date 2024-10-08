import uuid

from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db
from models.game_elements_tags_xref import game_elements_tags_xref


class Tags(db.Model):
    __tablename__ = "Tags"

    tag_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    type_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Types.type_id"), nullable=False)
    tag_name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String())

    type = db.relationship("Types", back_populates="tags")
    elements = db.relationship('GameElements', secondary=game_elements_tags_xref, back_populates='tags')

    def __init__(self, type_id, tag_name, description):
        self.type_id = type_id
        self.tag_name = tag_name
        self.description = description

    def new_tag_obj():
        return Tags("", "", "")
    

class TagsSchema(ma.Schema):
    class Meta:
        fields = ['tag_id', 'tag_name', 'description', 'type']
    type = ma.fields.Nested("TypesSchema")


tag_schema = TagsSchema()
tags_schema = TagsSchema(many=True)