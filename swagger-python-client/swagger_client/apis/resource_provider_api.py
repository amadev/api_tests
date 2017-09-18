# coding: utf-8

"""
    Placement API

    This is a sample server Placement API server.

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class ResourceProviderApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def delete_resource_provider(self, uuid, **kwargs):
        """
        Delete resource provider
        Delete the resource provider identified by `{uuid}`. This will also disassociate aggregates and delete inventories.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_resource_provider(uuid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str uuid: The uuid of a resource provider. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_resource_provider_with_http_info(uuid, **kwargs)
        else:
            (data) = self.delete_resource_provider_with_http_info(uuid, **kwargs)
            return data

    def delete_resource_provider_with_http_info(self, uuid, **kwargs):
        """
        Delete resource provider
        Delete the resource provider identified by `{uuid}`. This will also disassociate aggregates and delete inventories.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_resource_provider_with_http_info(uuid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str uuid: The uuid of a resource provider. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_resource_provider" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params) or (params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `delete_resource_provider`")


        collection_formats = {}

        resource_path = '/resource_providers/{uuid}'.replace('{format}', 'json')
        path_params = {}
        if 'uuid' in params:
            path_params['uuid'] = params['uuid']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)

    def show_resource_provider(self, uuid, **kwargs):
        """
        Show resource provider
        Return a representation of the resource provider identified by `{uuid}`.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.show_resource_provider(uuid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str uuid: The uuid of a resource provider. (required)
        :return: ResourceProvider
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.show_resource_provider_with_http_info(uuid, **kwargs)
        else:
            (data) = self.show_resource_provider_with_http_info(uuid, **kwargs)
            return data

    def show_resource_provider_with_http_info(self, uuid, **kwargs):
        """
        Show resource provider
        Return a representation of the resource provider identified by `{uuid}`.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.show_resource_provider_with_http_info(uuid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str uuid: The uuid of a resource provider. (required)
        :return: ResourceProvider
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method show_resource_provider" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params) or (params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `show_resource_provider`")


        collection_formats = {}

        resource_path = '/resource_providers/{uuid}'.replace('{format}', 'json')
        path_params = {}
        if 'uuid' in params:
            path_params['uuid'] = params['uuid']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ResourceProvider',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)

    def update_resource_provider(self, uuid, **kwargs):
        """
        Update resource provider
        Update the name of the resource provider identified by `{uuid}`.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_resource_provider(uuid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str uuid: The uuid of a resource provider. (required)
        :param Body1 body: 
        :return: ResourceProvider
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_resource_provider_with_http_info(uuid, **kwargs)
        else:
            (data) = self.update_resource_provider_with_http_info(uuid, **kwargs)
            return data

    def update_resource_provider_with_http_info(self, uuid, **kwargs):
        """
        Update resource provider
        Update the name of the resource provider identified by `{uuid}`.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_resource_provider_with_http_info(uuid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str uuid: The uuid of a resource provider. (required)
        :param Body1 body: 
        :return: ResourceProvider
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_resource_provider" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params) or (params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `update_resource_provider`")


        collection_formats = {}

        resource_path = '/resource_providers/{uuid}'.replace('{format}', 'json')
        path_params = {}
        if 'uuid' in params:
            path_params['uuid'] = params['uuid']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ResourceProvider',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)
