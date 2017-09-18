# swagger_client.ResourceProviderApi

All URIs are relative to *https://example.com/placement*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_resource_provider**](ResourceProviderApi.md#delete_resource_provider) | **DELETE** /resource_providers/{uuid} | Delete resource provider
[**show_resource_provider**](ResourceProviderApi.md#show_resource_provider) | **GET** /resource_providers/{uuid} | Show resource provider
[**update_resource_provider**](ResourceProviderApi.md#update_resource_provider) | **PUT** /resource_providers/{uuid} | Update resource provider


# **delete_resource_provider**
> delete_resource_provider(uuid)

Delete resource provider

Delete the resource provider identified by `{uuid}`. This will also disassociate aggregates and delete inventories.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
swagger_client.configuration.api_key['x-auth-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['x-auth-token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ResourceProviderApi()
uuid = 'uuid_example' # str | The uuid of a resource provider.

try: 
    # Delete resource provider
    api_instance.delete_resource_provider(uuid)
except ApiException as e:
    print("Exception when calling ResourceProviderApi->delete_resource_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The uuid of a resource provider. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_resource_provider**
> ResourceProvider show_resource_provider(uuid)

Show resource provider

Return a representation of the resource provider identified by `{uuid}`.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
swagger_client.configuration.api_key['x-auth-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['x-auth-token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ResourceProviderApi()
uuid = 'uuid_example' # str | The uuid of a resource provider.

try: 
    # Show resource provider
    api_response = api_instance.show_resource_provider(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceProviderApi->show_resource_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The uuid of a resource provider. | 

### Return type

[**ResourceProvider**](ResourceProvider.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_resource_provider**
> ResourceProvider update_resource_provider(uuid, body)

Update resource provider

Update the name of the resource provider identified by `{uuid}`.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
swagger_client.configuration.api_key['x-auth-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['x-auth-token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ResourceProviderApi()
uuid = 'uuid_example' # str | The uuid of a resource provider.
body = swagger_client.Body1() # Body1 | 

try: 
    # Update resource provider
    api_response = api_instance.update_resource_provider(uuid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceProviderApi->update_resource_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The uuid of a resource provider. | 
 **body** | [**Body1**](Body1.md)|  | 

### Return type

[**ResourceProvider**](ResourceProvider.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

