import uuid

from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db


class Types(db.Model):
    __tablename__ = "Types"

    type_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    collection_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Collections.collection_id"), nullable=False)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String())
    image_url = db.Column(db.String())
    color = db.Column(db.String())

    items = db.relationship("Items", foreign_keys="[Items.type_id]", back_populates="type", cascade='all')
    collection = db.relationship("Collections", back_populates="types")

    def __init__(self, name, description, image_url, color, collection_id):
        self.name = name
        self.description = description
        self.image_url = image_url
        self.color = color
        self.collection_id = collection_id

    def new_type_obj():
        return Types("", "", "", "", "", "", None)
    

class TypesSchema(ma.Schema):
    class Meta:
        fields = ['type_id', 'name', 'description', 'image_url', 'color', 'collection']
    collection = ma.fields.Nested("CollectionsSchema")


type_schema = TypesSchema()
types_schema = TypesSchema(many=True)