import uuid

from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db


class ReleaseProfiles(db.Model):
    __tablename__ = "ReleaseProfiles"

    profile_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    game_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Games.game_id", ondelete="CASCADE"), nullable=False)
    release_platforms = db.Column(db.String(), nullable=False)
    release_date = db.Column(db.String())
    developer = db.Column(db.String())
    publisher = db.Column(db.String())

    game = db.relationship("Games", back_populates="profile", uselist=False)

    def __init__(self, game_id, release_platforms, release_date, developer, publisher):
        self.game_id = game_id
        self.release_platforms = release_platforms
        self.release_date = release_date
        self.developer = developer
        self.publisher = publisher

    def new_profile_obj():
        return ReleaseProfiles("", "", "", "", "")


class ReleaseProfilesSchema(ma.Schema):
    class Meta:
        fields = ["profile_id", "release_platforms", "release_date", "developer", "publisher", "game"]
    game = ma.fields.Nested("GamesSchema")

release_profile_schema = ReleaseProfilesSchema()
release_profiles_schema = ReleaseProfilesSchema(many=True)