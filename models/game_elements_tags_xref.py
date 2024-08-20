import marshmallow as ma
from db import db

game_elements_tags_xref = db.Table(
    "GameElementsTagsXref",
    db.Model.metadata,
    db.Column('element_id', db.ForeignKey('GameElements.element_id', ondelete='CASCADE'), primary_key=True),
    db.Column('tag_id', db.ForeignKey('Tags.tag_id', ondelete='CASCADE'), primary_key=True)
)
