import uuid

from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db
from models.items_tags_xref import items_tags_xref


class Items(db.Model):
    __tablename__ = "Items"

    item_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    type_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Types.type_id"), nullable=False)
    collection_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Collections.collection_id"), nullable=False)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String())
    image_url = db.Column(db.String(), default=None)

    type = db.relationship("Types", back_populates="items")
    collection = db.relationship("Collections", back_populates="items")
    notes = db.relationship("Notes", back_populates="item", cascade="all")
    tags = db.relationship('Tags', secondary=items_tags_xref, back_populates='items')
    related_item_1 = db.relationship('Relationships', foreign_keys='Relationships.item_1_id', back_populates='item_1')
    related_item_2 = db.relationship('Relationships', foreign_keys='Relationships.item_2_id', back_populates='item_2')

    def __init__(self, name, description, type_id, collection_id, image_url=""):
        self.name = name
        self.description = description
        self.type_id = type_id
        self.collection_id = collection_id
        self.image_url = image_url

    def new_item_obj():
        return Items("", "", None, None, "")
    

class ItemsSchema(ma.Schema):
    class Meta:
        fields = ["item_id", "name", "description", "image_url", "type", "collection", "tags", "notes"]
    type = ma.fields.Nested("TypesSchema")
    collection = ma.fields.Nested("CollectionsSchema")
    tags = ma.fields.Nested("TagsSchema", many=True)
    notes = ma.fields.Nested("NotesSchema", many=True, exclude=["item"])


item_schema = ItemsSchema()
items_schema = ItemsSchema(many=True)