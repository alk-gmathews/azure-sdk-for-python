# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from typing import Optional, Dict, Any

from uamqp.constants import TransportType


class Configuration(object):  # pylint:disable=too-many-instance-attributes
    def __init__(self, **kwargs):
        self.user_agent = kwargs.get("user_agent")  # type: Optional[str]
        self.retry_total = kwargs.get("retry_total", 3)  # type: int
        self.retry_backoff_factor = kwargs.get("retry_backoff_factor", 0.8)  # type: float
        self.retry_backoff_max = kwargs.get("retry_backoff_max", 120)  # type: int
        self.logging_enable = kwargs.get("logging_enable", False)  # type: bool
        self.http_proxy = kwargs.get("http_proxy")  # type: Optional[Dict[str, Any]]
        self.transport_type = (
            TransportType.AmqpOverWebsocket
            if self.http_proxy
            else kwargs.get("transport_type", TransportType.Amqp)
        )
        self.auth_timeout = kwargs.get("auth_timeout", 60)  # type: int
        self.encoding = kwargs.get("encoding", "UTF-8")
        self.auto_reconnect = kwargs.get("auto_reconnect", True)
        self.idle_timeout = kwargs.get("idle_timeout", None)
        prefetch = kwargs.get("prefetch", 0)
        if int(prefetch) < 0 or int(prefetch) > 50000:
            raise ValueError("Prefetch must be an integer between 0 and 50000 inclusive.")
        self.prefetch = prefetch + 1
