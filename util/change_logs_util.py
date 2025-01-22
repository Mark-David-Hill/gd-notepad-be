# from sqlalchemy import event
from datetime import datetime

from ..models import ChangeLogs

import db


def log_changes(mapper, connection, target):
    """
    Log changes for a target model into the ChangeLogs table.
    """
    # Inspect the changes in the target model
    state = db.inspect(target)

    for attr in state.attrs:
        # Skip relationships or non-column attributes
        if not hasattr(attr, 'history'):
            continue

        history = attr.history
        if history.has_changes():
            old_value = history.deleted[0] if history.deleted else None
            new_value = history.added[0] if history.added else None

            # Only log if there is an actual change
            if old_value != new_value:
                change_log_entry = ChangeLogs(
                    table_name=target.__tablename__,
                    record_id=getattr(target, 'id', None),  # Assuming 'id' is the primary key
                    field_name=attr.key,
                    old_value=str(old_value) if old_value is not None else None,
                    new_value=str(new_value) if new_value is not None else None,
                    changed_by=getattr(target, 'updated_by', None),  # Assuming 'updated_by' is set on the target
                    changed_at=datetime.utcnow()
                )
                connection.execute(
                    db.insert(ChangeLogs).values(
                        table_name=change_log_entry.table_name,
                        record_id=change_log_entry.record_id,
                        field_name=change_log_entry.field_name,
                        old_value=change_log_entry.old_value,
                        new_value=change_log_entry.new_value,
                        changed_by=change_log_entry.changed_by,
                        changed_at=change_log_entry.changed_at,
                    )
                )