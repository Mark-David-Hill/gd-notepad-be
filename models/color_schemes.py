from datetime import datetime, timezone
import uuid

from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db


class ColorSchemes(db.Model):
    __tablename__ = "ColorSchemes"

    color_scheme_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(), nullable=False, unique=True)
    primary_color = db.Column(db.String(7), nullable=False)
    secondary_color = db.Column(db.String(7), nullable=True)
    text_color = db.Column(db.String(7), nullable=True)
    background_color = db.Column(db.String(7), nullable=True)

    types = db.relationship("Types", back_populates="color_scheme")

    def __init__(self, name, primary_color, secondary_color=None, text_color=None, background_color=None):
        self.name = name
        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.text_color = text_color
        self.background_color = background_color

    def new_color_scheme_obj():
        return ColorSchemes("", "", "", "", "")


class ColorSchemesSchema(ma.Schema):
    class Meta:
        fields = [
            "color_scheme_id",
            "name",
            "primary_color",
            "secondary_color",
            "text_color",
            "background_color",
        ]


color_scheme_schema = ColorSchemesSchema()
color_schemes_schema = ColorSchemesSchema(many=True)
