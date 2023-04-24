# Copyright 2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from flask import request
import marshmallow

from wazo_auth import exceptions, http, schemas
from wazo_auth.flask_helpers import Tenant
from wazo_auth.database.models import Session

from .schemas import session_create_schema


class Sessions(http.AuthResource):
    def __init__(self, session_service):
        self.session_service = session_service
        self.db_session = self.session_service._dao.session

    @http.required_acl('auth.sessions.create')
    def post(self):
        body = session_create_schema.load(request.get_json(force=True))
        session = Session(**body)
        self.db_session.add(session)
        self.db_session.flush()
        return session_create_schema.dump(session), 200
