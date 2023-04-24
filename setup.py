# Copyright 2016-2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from setuptools import find_packages
from setuptools import setup

setup(
    name='wazo_auth_session_create',
    version='1.0',
    description='Wazo auth',
    author='Wazo Authors',
    author_email='dev@wazo.community',
    url='http://wazo.community',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    package_data={
        'wazo_auth.plugins.http': ['*/api.yml'],
    },
    entry_points={
        'wazo_auth.http': [
            'session_create = wazo_auth_session_create.plugins.http.session_create.plugin:Plugin',
        ],
    },
)
