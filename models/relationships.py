import uuid

from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db


class Relationships(db.Model):
    __tablename__ = "Relationships"

    relationship_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    item_1_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Items.item_id"), nullable=False)
    item_2_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Items.item_id"), nullable=False)
    description = db.Column(db.String())
    count = db.Column(db.Integer(), default=0)

    item_1 = db.relationship("Items", foreign_keys=[item_1_id], back_populates="related_item_1")
    item_2 = db.relationship("Items", foreign_keys=[item_2_id], back_populates="related_item_2")

    def __init__(self, item_1_id, item_2_id, description, count=0):
        self.item_1_id = item_1_id
        self.item_2_id = item_2_id
        self.description = description
        self.count = count

    def new_relationship_obj():
        return Relationships("", "", "", 0)
    

class RelationshipsSchema(ma.Schema):
    class Meta:
        fields = ['relationship_id', 'item_1', 'item_2', 'description', 'count']
    item_1 = ma.fields.Nested("ItemsSchema")
    item_2 = ma.fields.Nested("ItemsSchema")


relationship_schema = RelationshipsSchema()
relationships_schema = RelationshipsSchema(many=True)