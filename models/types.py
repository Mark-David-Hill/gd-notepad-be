import uuid

from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db


class Types(db.Model):
    __tablename__ = "Types"

    type_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    collection_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Collections.collection_id"), nullable=False)
    color_scheme_id = db.Column(UUID(as_uuid=True), db.ForeignKey("ColorSchemes.color_scheme_id"), nullable=False)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String())
    image_url = db.Column(db.String())

    items = db.relationship("Items", foreign_keys="[Items.type_id]", back_populates="type", cascade='all')
    collection = db.relationship("Collections", back_populates="types")
    color_scheme = db.relationship("ColorSchemes", back_populates="types")

    def __init__(self, name, description, image_url, collection_id, color_scheme_id):
        self.name = name
        self.description = description
        self.image_url = image_url
        self.collection_id = collection_id
        self.color_scheme_id = color_scheme_id

    def new_type_obj():
        return Types("", "", "", None, None)
    

class TypesSchema(ma.Schema):
    class Meta:
        fields = ['type_id', 'name', 'description', 'image_url', 'collection', 'color_scheme']
    collection = ma.fields.Nested("CollectionsSchema")
    color_scheme = ma.fields.Nested("ColorSchemesSchema")


type_schema = TypesSchema()
types_schema = TypesSchema(many=True)