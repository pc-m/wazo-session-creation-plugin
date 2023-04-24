# Copyright 2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from xivo.mallow import fields

from wazo_auth.schemas import BaseSchema


class SessionCreateSchema(BaseSchema):
    uuid = fields.String(required=True)
    tenant_uuid = fields.String(required=True)
    user_uuid = fields.String(required=True)
    mobile = fields.Boolean(required=True)
    expiration = fields.Integer(required=True)


session_create_schema = SessionCreateSchema()