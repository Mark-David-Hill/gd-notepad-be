import uuid

from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db


class Types(db.Model):
    __tablename__ = "Types"

    type_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String())
    image_url = db.Column(db.String())
    color = db.Column(db.String())

    elements = db.relationship("GameElements", foreign_keys="[GameElements.type_id]", back_populates="type", cascade='all')
    tags = db.relationship("Tags", foreign_keys="[Tags.type_id]", back_populates="type", cascade='all')

    def __init__(self, name, description, image_url, color, light_color, dark_color):
        self.name = name
        self.description = description
        self.image_url = image_url
        self.color = color
        self.light_color = light_color
        self.dark_color = dark_color

    def new_type_obj():
        return Types("", "", "", "", "", "", "", "")
    

class TypesSchema(ma.Schema):
    class Meta:
        fields = ['type_id', 'name', 'description', 'image_url', 'color', 'light_color', 'dark_color']


type_schema = TypesSchema()
types_schema = TypesSchema(many=True)