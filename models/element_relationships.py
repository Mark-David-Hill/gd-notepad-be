import uuid

from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db


class ElementRelationships(db.Model):
    __tablename__ = "ElementRelationships"

    relationship_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    element_1_id = db.Column(UUID(as_uuid=True), db.ForeignKey("GameElements.element_id"), nullable=False)
    element_2_id = db.Column(UUID(as_uuid=True), db.ForeignKey("GameElements.element_id"), nullable=False)
    description = db.Column(db.String())
    count = db.Column(db.Integer(), default=0)

    element_1 = db.relationship("GameElements", foreign_keys=[element_1_id], back_populates="related_element_1")
    element_2 = db.relationship("GameElements", foreign_keys=[element_2_id], back_populates="related_element_2")

    def __init__(self, element_1_id, element_2_id, description, count=0):
        self.element_1_id = element_1_id
        self.element_2_id = element_2_id
        self.description = description
        self.count = count

    def new_relationship_obj():
        return ElementRelationships("", "", "", 0)
    

class ElementRelationshipsSchema(ma.Schema):
    class Meta:
        fields = ['relationship_id', 'element_1', 'element_2', 'description', 'count']
    element_1 = ma.fields.Nested("GameElementsSchema")
    element_2 = ma.fields.Nested("GameElementsSchema")


relationship_schema = ElementRelationshipsSchema()
relationships_schema = ElementRelationshipsSchema(many=True)