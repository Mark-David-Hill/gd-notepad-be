import uuid

from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db


class Games(db.Model):
    __tablename__ = "Games"

    game_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String())
    series = db.Column(db.String())
    genre = db.Column(db.String())

    elements = db.relationship("GameElements", foreign_keys="[GameElements.game_id]", back_populates="game", cascade='all')
    profile = db.relationship("ReleaseProfiles", back_populates="game", cascade="all", uselist=False)

    def __init__(self, name, description, series, genre):
        self.name = name
        self.description = description
        self.series = series
        self.genre = genre

    def new_game_obj():
        return Games("", "", "", "")
    

class GamesSchema(ma.Schema):
    class Meta:
        fields = ["game_id", "name", "description", "series", "genre"]

game_schema = GamesSchema()
games_schema = GamesSchema(many=True)