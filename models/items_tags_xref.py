import marshmallow as ma
from db import db

items_tags_xref = db.Table(
    "ItemsTagsXref",
    db.Model.metadata,
    db.Column('item_id', db.ForeignKey('Items.item_id', ondelete='CASCADE'), primary_key=True),
    db.Column('tag_id', db.ForeignKey('Tags.tag_id', ondelete='CASCADE'), primary_key=True)
)
