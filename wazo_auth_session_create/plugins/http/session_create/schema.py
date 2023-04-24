# Copyright 2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from xivo.mallow import fields

from wazo_auth.schemas import BaseSchema


class SessionCreateSchema(BaseSchema):
    uuid = fields.String()
    tenant_uuid = fields.String()
    user_uuid = fields.String()
    mobile = fields.Boolean()


session_create_schema = SessionCreateSchema()