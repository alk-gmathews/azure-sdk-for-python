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

try:
    from ._models_py3 import DataContainer
    from ._models_py3 import Error
    from ._models_py3 import ProxyResource
    from ._models_py3 import ResponseWithError, ResponseWithErrorException
    from ._models_py3 import VMInsightsOnboardingStatus
    from ._models_py3 import WorkspaceInfo
except (SyntaxError, ImportError):
    from ._models import DataContainer
    from ._models import Error
    from ._models import ProxyResource
    from ._models import ResponseWithError, ResponseWithErrorException
    from ._models import VMInsightsOnboardingStatus
    from ._models import WorkspaceInfo
from ._monitor_management_client_enums import (
    OnboardingStatus,
    DataStatus,
)

__all__ = [
    'DataContainer',
    'Error',
    'ProxyResource',
    'ResponseWithError', 'ResponseWithErrorException',
    'VMInsightsOnboardingStatus',
    'WorkspaceInfo',
    'OnboardingStatus',
    'DataStatus',
]