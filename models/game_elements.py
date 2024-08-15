import uuid

from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db


class GameElements(db.Model):
    __tablename__ = "GameElements"

    element_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    type_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Types.type_id"), nullable=False)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String())
    image_url = db.Column(db.String())

    type = db.relationship("Types", back_populates="elements")
    note = db.relationship("Notes", back_populates="element", cascade="all")

    def __init__(self, name, description, image_url):
        self.name = name
        self.description = description
        self.image_url = image_url

    def new_element_obj():
        return GameElements("", "", "")
    

class GameElementsSchema(ma.Schema):
    class Meta:
        fields = ["element_id", "name", "description", "image_url", "type"]
    type = ma.fields.Nested("TypesSchema")


game_element_schema = GameElementsSchema()
game_elements_schema = GameElementsSchema(many=True)