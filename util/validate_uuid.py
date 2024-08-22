from flask import jsonify
from uuid import UUID

def validate_uuid(id): 
    try:
        UUID(id, version=4)
    except Exception as e:
        return False
    
    return True