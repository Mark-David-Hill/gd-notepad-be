import uuid

from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db
from models.game_elements_tags_xref import game_elements_tags_xref


class GameElements(db.Model):
    __tablename__ = "GameElements"

    element_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    type_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Types.type_id"), nullable=False)
    collection_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Collections.collection_id"), nullable=False)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String())
    image_url = db.Column(db.String(), default=None)

    type = db.relationship("Types", back_populates="elements")
    collection = db.relationship("Collections", back_populates="elements")
    notes = db.relationship("Notes", back_populates="element", cascade="all")
    tags = db.relationship('Tags', secondary=game_elements_tags_xref, back_populates='elements')
    related_element_1 = db.relationship('ElementRelationships', foreign_keys='ElementRelationships.element_1_id', back_populates='element_1')
    related_element_2 = db.relationship('ElementRelationships', foreign_keys='ElementRelationships.element_2_id', back_populates='element_2')

    def __init__(self, name, description, type_id, collection_id, image_url=""):
        self.name = name
        self.description = description
        self.type_id = type_id
        self.collection_id = collection_id
        self.image_url = image_url

    def new_element_obj():
        return GameElements("", "", None, None, "")
    

class GameElementsSchema(ma.Schema):
    class Meta:
        fields = ["element_id", "name", "description", "image_url", "type", "collection", "tags", "notes"]
    type = ma.fields.Nested("TypesSchema")
    collection = ma.fields.Nested("CollectionsSchema")
    tags = ma.fields.Nested("TagsSchema", many=True, exclude=["type"])
    notes = ma.fields.Nested("NotesSchema", many=True, exclude=["element"])


game_element_schema = GameElementsSchema()
game_elements_schema = GameElementsSchema(many=True)