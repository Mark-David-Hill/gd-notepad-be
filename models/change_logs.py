import uuid
from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db


class ChangeLogs(db.Model):
    __tablename__ = "ChangeLogs"

    change_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    table_name = db.Column(db.String(), nullable=False)
    record_id = db.Column(UUID(as_uuid=True), nullable=False)
    field_name = db.Column(db.String(), nullable=True)
    old_value = db.Column(db.Text(), nullable=True)
    new_value = db.Column(db.Text(), nullable=True)
    user_changed_by = db.Column(UUID(as_uuid=True), db.ForeignKey("Users.user_id"), nullable=False)
    date_changed = db.Column(db.DateTime(), nullable=False, default=db.func.now())

    user = db.relationship("Users", back_populates="change_logs")

    def __init__(self, table_name, record_id, field_name, old_value, new_value, user_changed_by):
        self.table_name = table_name
        self.record_id = record_id
        self.field_name = field_name
        self.old_value = old_value
        self.new_value = new_value
        self.user_changed_by = user_changed_by


class ChangeLogsSchema(ma.Schema):
    class Meta:
        fields = [
            "change_id",
            "table_name",
            "record_id",
            "field_name",
            "old_value",
            "new_value",
            "user_changed_by",
            "date_changed",
        ]


change_log_schema = ChangeLogsSchema()
change_logs_schema = ChangeLogsSchema(many=True)
