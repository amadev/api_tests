# swagger_client.ResourceProvidersApi

All URIs are relative to *https://localhost:9000/placement*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_resource_provider**](ResourceProvidersApi.md#create_resource_provider) | **POST** /resource_providers | Create resource provider
[**show_resource_providers**](ResourceProvidersApi.md#show_resource_providers) | **GET** /resource_providers | List resource providers


# **create_resource_provider**
> create_resource_provider(body)

Create resource provider

Create a new resource provider.

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
api_instance = swagger_client.ResourceProvidersApi()
body = swagger_client.Body() # Body | order placed for purchasing the pet

try: 
    # Create resource provider
    api_instance.create_resource_provider(body)
except ApiException as e:
    print("Exception when calling ResourceProvidersApi->create_resource_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)| order placed for purchasing the pet | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_resource_providers**
> InlineResponse200 show_resource_providers(resources_query=resources_query, member_of=member_of, uuid=uuid, name=name)

List resource providers

List an optionally filtered collection of resource providers

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
api_instance = swagger_client.ResourceProvidersApi()
resources_query = 'resources_query_example' # str | A comma-separated list of strings indicating an amount of resource of a specified class that a provider must have the capacity to serve:: resources=VCPU:4,DISK_GB:64,MEMORY_MB:2048 (optional)
member_of = 'member_of_example' # str | A comma-separated list of strings representing aggregate uuids. The returned resource providers must be associated with at least one of the aggregates identified by uuid. (optional)
uuid = 'uuid_example' # str | The uuid of a resource provider. (optional)
name = 'name_example' # str | The name of a resource provider. (optional)

try: 
    # List resource providers
    api_response = api_instance.show_resource_providers(resources_query=resources_query, member_of=member_of, uuid=uuid, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourceProvidersApi->show_resource_providers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resources_query** | **str**| A comma-separated list of strings indicating an amount of resource of a specified class that a provider must have the capacity to serve:: resources&#x3D;VCPU:4,DISK_GB:64,MEMORY_MB:2048 | [optional] 
 **member_of** | **str**| A comma-separated list of strings representing aggregate uuids. The returned resource providers must be associated with at least one of the aggregates identified by uuid. | [optional] 
 **uuid** | **str**| The uuid of a resource provider. | [optional] 
 **name** | **str**| The name of a resource provider. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

