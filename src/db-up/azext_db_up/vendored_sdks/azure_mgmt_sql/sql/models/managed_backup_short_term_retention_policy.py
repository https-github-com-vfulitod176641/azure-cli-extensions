# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .proxy_resource import ProxyResource


class ManagedBackupShortTermRetentionPolicy(ProxyResource):
    """A short term retention policy.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param retention_days: The backup retention period in days. This is how
     many days Point-in-Time Restore will be supported.
    :type retention_days: int
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'retention_days': {'key': 'properties.retentionDays', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(ManagedBackupShortTermRetentionPolicy, self).__init__(**kwargs)
        self.retention_days = kwargs.get('retention_days', None)
