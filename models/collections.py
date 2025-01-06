import uuid

from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db


class Collections(db.Model):
    __tablename__ = "Collections"

    collection_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String())
    series = db.Column(db.String())
    genre = db.Column(db.String())
    image_url = db.Column(db.String(), default="")

    elements = db.relationship("GameElements", foreign_keys="[GameElements.collection_id]", back_populates="collection", cascade='all')

    def __init__(self, name, description, series, genre, image_url):
        self.name = name
        self.description = description
        self.series = series
        self.genre = genre
        self.image_url = image_url

    def new_collection_obj():
        return Collections("", "", "", "", "")
    

class CollectionsSchema(ma.Schema):
    class Meta:
        fields = ["collection_id", "name", "description", "series", "genre", "image_url"]

collection_schema = CollectionsSchema()
collections_schema = CollectionsSchema(many=True)