# Copyright 2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from . import http


class Plugin:
    def load(self, dependencies):
        api = dependencies['api']
        session_service = dependencies['session_service']

        api.add_resource(
            http.Sessions,
            '/sessions2',
            resource_class_args=[session_service],
        )
