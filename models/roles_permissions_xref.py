import marshmallow as ma
from db import db

roles_permissions_xref = db.Table(
    "RolesPermissionsXref",
    db.Model.metadata,
    db.Column('role_id', db.ForeignKey('Roles.role_id', ondelete='CASCADE'), primary_key=True),
    db.Column('permission_id', db.ForeignKey('Permissions.permission_id', ondelete='CASCADE'), primary_key=True)
)
