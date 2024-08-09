from flask import jsonify, request
import functools
from datetime import datetime
from uuid import UUID

from db import db
# from models.auth_tokens import AuthTokens