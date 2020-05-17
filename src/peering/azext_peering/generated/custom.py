# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

import json


def peering__check_service_provider_availability(cmd, client,
                                                 peering_service_location=None,
                                                 peering_service_provider=None):
    return client.check_service_provider_availability(peering_service_location=peering_service_location,
                                                      peering_service_provider=peering_service_provider)


def peering_legacy_peering_list(cmd, client,
                                peering_location,
                                kind,
                                asn=None):
    return client.list(peering_location=peering_location,
                       kind=kind,
                       asn=asn)


def peering_peering_asn_list(cmd, client):
    return client.list_by_subscription()


def peering_peering_asn_show(cmd, client,
                             peer_asn_name):
    return client.get(peer_asn_name=peer_asn_name)


def peering_peering_asn_create(cmd, client,
                               peer_asn_name,
                               peer_asn=None,
                               peer_contact_detail=None,
                               peer_name=None,
                               validation_state=None):
    return client.create_or_update(peer_asn_name=peer_asn_name,
                                   peer_asn=peer_asn,
                                   peer_contact_detail=peer_contact_detail,
                                   peer_name=peer_name,
                                   validation_state=validation_state)


def peering_peering_asn_update(instance, cmd,
                               peer_asn_name,
                               peer_asn=None,
                               peer_contact_detail=None,
                               peer_name=None,
                               validation_state=None):
    return instance


def peering_peering_asn_delete(cmd, client,
                               peer_asn_name):
    return client.delete(peer_asn_name=peer_asn_name)


def peering_peering_location_list(cmd, client,
                                  kind,
                                  direct_peering_type=None):
    return client.list(kind=kind,
                       direct_peering_type=direct_peering_type)


def peering_registered_asn_list(cmd, client,
                                resource_group_name,
                                peering_name):
    return client.list_by_peering(resource_group_name=resource_group_name,
                                  peering_name=peering_name)


def peering_registered_asn_show(cmd, client,
                                resource_group_name,
                                peering_name,
                                registered_asn_name):
    return client.get(resource_group_name=resource_group_name,
                      peering_name=peering_name,
                      registered_asn_name=registered_asn_name)


def peering_registered_asn_create(cmd, client,
                                  resource_group_name,
                                  peering_name,
                                  registered_asn_name,
                                  asn=None):
    return client.create_or_update(resource_group_name=resource_group_name,
                                   peering_name=peering_name,
                                   registered_asn_name=registered_asn_name,
                                   asn=asn)


def peering_registered_asn_update(cmd, client,
                                  resource_group_name,
                                  peering_name,
                                  registered_asn_name,
                                  asn=None):
    return client.create_or_update(resource_group_name=resource_group_name,
                                   peering_name=peering_name,
                                   registered_asn_name=registered_asn_name,
                                   asn=asn)


def peering_registered_asn_delete(cmd, client,
                                  resource_group_name,
                                  peering_name,
                                  registered_asn_name):
    return client.delete(resource_group_name=resource_group_name,
                         peering_name=peering_name,
                         registered_asn_name=registered_asn_name)


def peering_registered_prefix_list(cmd, client,
                                   resource_group_name,
                                   peering_name):
    return client.list_by_peering(resource_group_name=resource_group_name,
                                  peering_name=peering_name)


def peering_registered_prefix_show(cmd, client,
                                   resource_group_name,
                                   peering_name,
                                   registered_prefix_name):
    return client.get(resource_group_name=resource_group_name,
                      peering_name=peering_name,
                      registered_prefix_name=registered_prefix_name)


def peering_registered_prefix_create(cmd, client,
                                     resource_group_name,
                                     peering_name,
                                     registered_prefix_name,
                                     prefix=None):
    return client.create_or_update(resource_group_name=resource_group_name,
                                   peering_name=peering_name,
                                   registered_prefix_name=registered_prefix_name,
                                   prefix=prefix)


def peering_registered_prefix_update(cmd, client,
                                     resource_group_name,
                                     peering_name,
                                     registered_prefix_name,
                                     prefix=None):
    return client.create_or_update(resource_group_name=resource_group_name,
                                   peering_name=peering_name,
                                   registered_prefix_name=registered_prefix_name,
                                   prefix=prefix)


def peering_registered_prefix_delete(cmd, client,
                                     resource_group_name,
                                     peering_name,
                                     registered_prefix_name):
    return client.delete(resource_group_name=resource_group_name,
                         peering_name=peering_name,
                         registered_prefix_name=registered_prefix_name)


def peering_peering_list(cmd, client,
                         resource_group_name=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name)
    return client.list_by_subscription()


def peering_peering_show(cmd, client,
                         resource_group_name,
                         peering_name):
    return client.get(resource_group_name=resource_group_name,
                      peering_name=peering_name)


def peering_peering_create(cmd, client,
                           resource_group_name,
                           peering_name,
                           sku,
                           kind,
                           location,
                           tags=None,
                           direct=None,
                           exchange=None,
                           peering_location=None):
    if isinstance(direct, str):
        direct = json.loads(direct)
    if isinstance(exchange, str):
        exchange = json.loads(exchange)
    return client.create_or_update(resource_group_name=resource_group_name,
                                   peering_name=peering_name,
                                   sku=sku,
                                   kind=kind,
                                   location=location,
                                   tags=tags,
                                   direct=direct,
                                   exchange=exchange,
                                   peering_location=peering_location)


def peering_peering_update(cmd, client,
                           resource_group_name,
                           peering_name,
                           tags=None):
    return client.update(resource_group_name=resource_group_name,
                         peering_name=peering_name,
                         tags=tags)


def peering_peering_delete(cmd, client,
                           resource_group_name,
                           peering_name):
    return client.delete(resource_group_name=resource_group_name,
                         peering_name=peering_name)


def peering_received_route_list(cmd, client,
                                resource_group_name,
                                peering_name,
                                prefix=None,
                                as_path=None,
                                origin_as_validation_state=None,
                                rpki_validation_state=None,
                                skip_token=None):
    return client.list_by_peering(resource_group_name=resource_group_name,
                                  peering_name=peering_name,
                                  prefix=prefix,
                                  as_path=as_path,
                                  origin_as_validation_state=origin_as_validation_state,
                                  rpki_validation_state=rpki_validation_state,
                                  skip_token=skip_token)


def peering_peering_service_country_list(cmd, client):
    return client.list()


def peering_peering_service_location_list(cmd, client,
                                          country=None):
    return client.list(country=country)


def peering_prefix_list(cmd, client,
                        resource_group_name,
                        peering_service_name,
                        expand=None):
    return client.list_by_peering_service(resource_group_name=resource_group_name,
                                          peering_service_name=peering_service_name,
                                          expand=expand)


def peering_prefix_show(cmd, client,
                        resource_group_name,
                        peering_service_name,
                        prefix_name,
                        expand=None):
    return client.get(resource_group_name=resource_group_name,
                      peering_service_name=peering_service_name,
                      prefix_name=prefix_name,
                      expand=expand)


def peering_prefix_create(cmd, client,
                          resource_group_name,
                          peering_service_name,
                          prefix_name,
                          prefix=None,
                          peering_service_prefix_key=None):
    return client.create_or_update(resource_group_name=resource_group_name,
                                   peering_service_name=peering_service_name,
                                   prefix_name=prefix_name,
                                   prefix=prefix,
                                   peering_service_prefix_key=peering_service_prefix_key)


def peering_prefix_update(cmd, client,
                          resource_group_name,
                          peering_service_name,
                          prefix_name,
                          prefix=None,
                          peering_service_prefix_key=None):
    return client.create_or_update(resource_group_name=resource_group_name,
                                   peering_service_name=peering_service_name,
                                   prefix_name=prefix_name,
                                   prefix=prefix,
                                   peering_service_prefix_key=peering_service_prefix_key)


def peering_prefix_delete(cmd, client,
                          resource_group_name,
                          peering_service_name,
                          prefix_name):
    return client.delete(resource_group_name=resource_group_name,
                         peering_service_name=peering_service_name,
                         prefix_name=prefix_name)


def peering_peering_service_provider_list(cmd, client):
    return client.list()


def peering_peering_service_list(cmd, client,
                                 resource_group_name=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name)
    return client.list_by_subscription()


def peering_peering_service_show(cmd, client,
                                 resource_group_name,
                                 peering_service_name):
    return client.get(resource_group_name=resource_group_name,
                      peering_service_name=peering_service_name)


def peering_peering_service_create(cmd, client,
                                   resource_group_name,
                                   peering_service_name,
                                   location,
                                   sku=None,
                                   tags=None,
                                   peering_service_location=None,
                                   peering_service_provider=None):
    return client.create_or_update(resource_group_name=resource_group_name,
                                   peering_service_name=peering_service_name,
                                   sku=sku,
                                   location=location,
                                   tags=tags,
                                   peering_service_location=peering_service_location,
                                   peering_service_provider=peering_service_provider)


def peering_peering_service_update(cmd, client,
                                   resource_group_name,
                                   peering_service_name,
                                   tags=None):
    return client.update(resource_group_name=resource_group_name,
                         peering_service_name=peering_service_name,
                         tags=tags)


def peering_peering_service_delete(cmd, client,
                                   resource_group_name,
                                   peering_service_name):
    return client.delete(resource_group_name=resource_group_name,
                         peering_service_name=peering_service_name)
