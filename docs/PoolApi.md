# exapi_client_python.PoolApi

All URIs are relative to *https://api.exkoin.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**private_pool_join_post**](PoolApi.md#private_pool_join_post) | **POST** /private/pool/join | 
[**private_pool_leave_post**](PoolApi.md#private_pool_leave_post) | **POST** /private/pool/leave | 
[**private_pool_task_get**](PoolApi.md#private_pool_task_get) | **GET** /private/pool/task | 
[**private_pool_tasks_get**](PoolApi.md#private_pool_tasks_get) | **GET** /private/pool/tasks | 
[**public_pools_get**](PoolApi.md#public_pools_get) | **GET** /public/pools | 


# **private_pool_join_post**
> PrivatePoolJoinPost200Response private_pool_join_post(private_pool_join_post_request)

Join a pool, it will deduct the currencies from your balance, and you will be credited the corresponding lp token

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (signature):
* Basic Authentication (basicAuth):
* Api Key Authentication (sessionToken):
* Api Key Authentication (nonce):

```python
import exapi_client_python
from exapi_client_python.models.private_pool_join_post200_response import PrivatePoolJoinPost200Response
from exapi_client_python.models.private_pool_join_post_request import PrivatePoolJoinPostRequest
from exapi_client_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.exkoin.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = exapi_client_python.Configuration(
    host = "https://api.exkoin.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: signature
configuration.api_key['signature'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['signature'] = 'Bearer'

# Configure HTTP basic authorization: basicAuth
configuration = exapi_client_python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: sessionToken
configuration.api_key['sessionToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionToken'] = 'Bearer'

# Configure API key authorization: nonce
configuration.api_key['nonce'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['nonce'] = 'Bearer'

# Enter a context with an instance of the API client
with exapi_client_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = exapi_client_python.PoolApi(api_client)
    private_pool_join_post_request = exapi_client_python.PrivatePoolJoinPostRequest() # PrivatePoolJoinPostRequest | 

    try:
        api_response = api_instance.private_pool_join_post(private_pool_join_post_request)
        print("The response of PoolApi->private_pool_join_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoolApi->private_pool_join_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **private_pool_join_post_request** | [**PrivatePoolJoinPostRequest**](PrivatePoolJoinPostRequest.md)|  | 

### Return type

[**PrivatePoolJoinPost200Response**](PrivatePoolJoinPost200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [signature](../README.md#signature), [basicAuth](../README.md#basicAuth), [sessionToken](../README.md#sessionToken), [nonce](../README.md#nonce)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |
**0** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_pool_leave_post**
> PrivatePoolJoinPost200Response private_pool_leave_post(private_pool_leave_post_request)

Leave a pool, it consumes the lp token and credits your balance with the corresponding currencies

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (signature):
* Basic Authentication (basicAuth):
* Api Key Authentication (sessionToken):
* Api Key Authentication (nonce):

```python
import exapi_client_python
from exapi_client_python.models.private_pool_join_post200_response import PrivatePoolJoinPost200Response
from exapi_client_python.models.private_pool_leave_post_request import PrivatePoolLeavePostRequest
from exapi_client_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.exkoin.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = exapi_client_python.Configuration(
    host = "https://api.exkoin.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: signature
configuration.api_key['signature'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['signature'] = 'Bearer'

# Configure HTTP basic authorization: basicAuth
configuration = exapi_client_python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: sessionToken
configuration.api_key['sessionToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionToken'] = 'Bearer'

# Configure API key authorization: nonce
configuration.api_key['nonce'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['nonce'] = 'Bearer'

# Enter a context with an instance of the API client
with exapi_client_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = exapi_client_python.PoolApi(api_client)
    private_pool_leave_post_request = exapi_client_python.PrivatePoolLeavePostRequest() # PrivatePoolLeavePostRequest | 

    try:
        api_response = api_instance.private_pool_leave_post(private_pool_leave_post_request)
        print("The response of PoolApi->private_pool_leave_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoolApi->private_pool_leave_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **private_pool_leave_post_request** | [**PrivatePoolLeavePostRequest**](PrivatePoolLeavePostRequest.md)|  | 

### Return type

[**PrivatePoolJoinPost200Response**](PrivatePoolJoinPost200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [signature](../README.md#signature), [basicAuth](../README.md#basicAuth), [sessionToken](../README.md#sessionToken), [nonce](../README.md#nonce)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |
**0** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_pool_task_get**
> PrivatePoolTasksGet200ResponseInner private_pool_task_get(task_id)

get a pool task (join/leave) by id

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (signature):
* Basic Authentication (basicAuth):
* Api Key Authentication (sessionToken):
* Api Key Authentication (nonce):

```python
import exapi_client_python
from exapi_client_python.models.private_pool_tasks_get200_response_inner import PrivatePoolTasksGet200ResponseInner
from exapi_client_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.exkoin.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = exapi_client_python.Configuration(
    host = "https://api.exkoin.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: signature
configuration.api_key['signature'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['signature'] = 'Bearer'

# Configure HTTP basic authorization: basicAuth
configuration = exapi_client_python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: sessionToken
configuration.api_key['sessionToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionToken'] = 'Bearer'

# Configure API key authorization: nonce
configuration.api_key['nonce'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['nonce'] = 'Bearer'

# Enter a context with an instance of the API client
with exapi_client_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = exapi_client_python.PoolApi(api_client)
    task_id = 'task_id_example' # str | 

    try:
        api_response = api_instance.private_pool_task_get(task_id)
        print("The response of PoolApi->private_pool_task_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoolApi->private_pool_task_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 

### Return type

[**PrivatePoolTasksGet200ResponseInner**](PrivatePoolTasksGet200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey), [signature](../README.md#signature), [basicAuth](../README.md#basicAuth), [sessionToken](../README.md#sessionToken), [nonce](../README.md#nonce)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |
**0** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_pool_tasks_get**
> List[PrivatePoolTasksGet200ResponseInner] private_pool_tasks_get(pool_id=pool_id, type=type, status=status, page=page, limit=limit, start_time=start_time, end_time=end_time)

Get the user pool tasks (join/leave)

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (signature):
* Basic Authentication (basicAuth):
* Api Key Authentication (sessionToken):
* Api Key Authentication (nonce):

```python
import exapi_client_python
from exapi_client_python.models.private_pool_tasks_get200_response_inner import PrivatePoolTasksGet200ResponseInner
from exapi_client_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.exkoin.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = exapi_client_python.Configuration(
    host = "https://api.exkoin.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: signature
configuration.api_key['signature'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['signature'] = 'Bearer'

# Configure HTTP basic authorization: basicAuth
configuration = exapi_client_python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: sessionToken
configuration.api_key['sessionToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionToken'] = 'Bearer'

# Configure API key authorization: nonce
configuration.api_key['nonce'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['nonce'] = 'Bearer'

# Enter a context with an instance of the API client
with exapi_client_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = exapi_client_python.PoolApi(api_client)
    pool_id = 'pool_id_example' # str |  (optional)
    type = 'type_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    page = 3.4 # float |  (optional)
    limit = 3.4 # float |  (optional)
    start_time = 3.4 # float |  (optional)
    end_time = 3.4 # float |  (optional)

    try:
        api_response = api_instance.private_pool_tasks_get(pool_id=pool_id, type=type, status=status, page=page, limit=limit, start_time=start_time, end_time=end_time)
        print("The response of PoolApi->private_pool_tasks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoolApi->private_pool_tasks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **page** | **float**|  | [optional] 
 **limit** | **float**|  | [optional] 
 **start_time** | **float**|  | [optional] 
 **end_time** | **float**|  | [optional] 

### Return type

[**List[PrivatePoolTasksGet200ResponseInner]**](PrivatePoolTasksGet200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey), [signature](../README.md#signature), [basicAuth](../README.md#basicAuth), [sessionToken](../README.md#sessionToken), [nonce](../README.md#nonce)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |
**0** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_pools_get**
> List[PublicPoolsGet200ResponseInner] public_pools_get()

Get all active pools

### Example


```python
import exapi_client_python
from exapi_client_python.models.public_pools_get200_response_inner import PublicPoolsGet200ResponseInner
from exapi_client_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.exkoin.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = exapi_client_python.Configuration(
    host = "https://api.exkoin.com/v1"
)


# Enter a context with an instance of the API client
with exapi_client_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = exapi_client_python.PoolApi(api_client)

    try:
        api_response = api_instance.public_pools_get()
        print("The response of PoolApi->public_pools_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoolApi->public_pools_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PublicPoolsGet200ResponseInner]**](PublicPoolsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |
**0** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

