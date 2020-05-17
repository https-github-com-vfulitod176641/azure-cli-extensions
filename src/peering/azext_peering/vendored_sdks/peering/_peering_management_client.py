# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

from ._configuration import PeeringManagementClientConfiguration
from .operations import PeeringManagementClientOperationsMixin
from .operations import LegacyPeeringOperations
from .operations import OperationOperations
from .operations import PeerAsnOperations
from .operations import PeeringLocationOperations
from .operations import RegisteredAsnOperations
from .operations import RegisteredPrefixOperations
from .operations import PeeringOperations
from .operations import ReceivedRouteOperations
from .operations import PeeringServiceCountryOperations
from .operations import PeeringServiceLocationOperations
from .operations import PrefixOperations
from .operations import PeeringServiceProviderOperations
from .operations import PeeringServiceOperations
from . import models


class PeeringManagementClient(PeeringManagementClientOperationsMixin):
    """Peering Client.

    :ivar legacy_peering: LegacyPeeringOperations operations
    :vartype legacy_peering: azure.mgmt.peering.operations.LegacyPeeringOperations
    :ivar operation: OperationOperations operations
    :vartype operation: azure.mgmt.peering.operations.OperationOperations
    :ivar peer_asn: PeerAsnOperations operations
    :vartype peer_asn: azure.mgmt.peering.operations.PeerAsnOperations
    :ivar peering_location: PeeringLocationOperations operations
    :vartype peering_location: azure.mgmt.peering.operations.PeeringLocationOperations
    :ivar registered_asn: RegisteredAsnOperations operations
    :vartype registered_asn: azure.mgmt.peering.operations.RegisteredAsnOperations
    :ivar registered_prefix: RegisteredPrefixOperations operations
    :vartype registered_prefix: azure.mgmt.peering.operations.RegisteredPrefixOperations
    :ivar peering: PeeringOperations operations
    :vartype peering: azure.mgmt.peering.operations.PeeringOperations
    :ivar received_route: ReceivedRouteOperations operations
    :vartype received_route: azure.mgmt.peering.operations.ReceivedRouteOperations
    :ivar peering_service_country: PeeringServiceCountryOperations operations
    :vartype peering_service_country: azure.mgmt.peering.operations.PeeringServiceCountryOperations
    :ivar peering_service_location: PeeringServiceLocationOperations operations
    :vartype peering_service_location: azure.mgmt.peering.operations.PeeringServiceLocationOperations
    :ivar prefix: PrefixOperations operations
    :vartype prefix: azure.mgmt.peering.operations.PrefixOperations
    :ivar peering_service_provider: PeeringServiceProviderOperations operations
    :vartype peering_service_provider: azure.mgmt.peering.operations.PeeringServiceProviderOperations
    :ivar peering_service: PeeringServiceOperations operations
    :vartype peering_service: azure.mgmt.peering.operations.PeeringServiceOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = PeeringManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.legacy_peering = LegacyPeeringOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operation = OperationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.peer_asn = PeerAsnOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.peering_location = PeeringLocationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.registered_asn = RegisteredAsnOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.registered_prefix = RegisteredPrefixOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.peering = PeeringOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.received_route = ReceivedRouteOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.peering_service_country = PeeringServiceCountryOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.peering_service_location = PeeringServiceLocationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.prefix = PrefixOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.peering_service_provider = PeeringServiceProviderOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.peering_service = PeeringServiceOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> PeeringManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
