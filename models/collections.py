from datetime import datetime, timezone
import uuid

from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db


class Collections(db.Model):
    __tablename__ = "Collections"

    collection_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String())
    image_url = db.Column(db.String(), default="")
    date_created = db.Column(db.DateTime(timezone=True), default=datetime.now(timezone.utc), nullable=False)
    date_updated = db.Column(db.DateTime(timezone=True), default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc), nullable=False)
    private = db.Column(db.Boolean(), nullable=False, default=False)
    active = db.Column(db.Boolean(), nullable=False, default=True)
    owner_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Users.user_id"), nullable=False)

    owner = db.relationship("Users", back_populates="collections_owned")
    items = db.relationship("Items", foreign_keys="[Items.collection_id]", back_populates="collection", cascade='all')
    types = db.relationship("Types", foreign_keys="[Types.collection_id]", back_populates="collection", cascade='all')
    tags = db.relationship("Tags", foreign_keys="[Tags.collection_id]", back_populates="collection", cascade='all')

    def __init__(self, name, description, image_url, private=False):
        self.name = name
        self.description = description
        self.image_url = image_url
        self.private = private

    def new_collection_obj():
        return Collections("", "", "", False)


class CollectionsSchema(ma.Schema):
    class Meta:
        fields = [
            "collection_id",
            "name",
            "description",
            "image_url",
            "date_created",
            "date_updated",
            "private",
            "active",
            "owner_id",
        ]


collection_schema = CollectionsSchema()
collections_schema = CollectionsSchema(many=True)