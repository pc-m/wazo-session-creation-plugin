# Copyright 2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from flask import request
import marshmallow
import time
import os
from sqlalchemy import exc

from xivo.rest_api_helpers import APIException
from wazo_auth import exceptions, http, schemas
from wazo_auth.flask_helpers import Tenant
from wazo_auth.database.models import Session, Token

from .schemas import session_create_schema

DEFAULT_XIVO_UUID = os.getenv('XIVO_UUID')


class Sessions(http.AuthResource):
    def __init__(self, session_service):
        self.session_service = session_service
        self.db_session = self.session_service._dao.session.session

    @http.required_acl('auth.sessions.create')
    def post(self):
        body = session_create_schema.load(request.get_json(force=True))
        current_time = time.time()
        expiration_time = current_time + body['expiration']
        user_agent = request.headers.get('User-Agent', '')
        remote_addr = request.remote_addr

        token = Token(
            auth_id=body['user_uuid'],
            pbx_user_uuid=body['user_uuid'],
            xivo_uuid=DEFAULT_XIVO_UUID,
            issued_t=int(current_time),
            expire_t=int(expiration_time),
            user_agent=user_agent,
            remote_addr=remote_addr,
            metadata={},
            acl=[],
        )
        token.session = Session(
            uuid=body['uuid'],
            tenant_uuid=body['tenant_uuid'],
            mobile=body['mobile'],
        )
        self.db_session.add(token)
        try:
            self.db_session.flush()
        except exc.IntegrityError as e:
            self.db_session.rollback()
            if e.orig.pgcode == '23505':
                raise APIException(
                    409,
                    'Duplicate session',
                    'duplicate_session',
                    {'session_uuid': body['uuid']},
                    'sessions2',
                )
        return body, 200
