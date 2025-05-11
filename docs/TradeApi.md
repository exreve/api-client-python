# exapi_client_python.TradeApi

All URIs are relative to *https://api.exkoin.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**private_orders_cancel_post**](TradeApi.md#private_orders_cancel_post) | **POST** /private/orders/cancel | 
[**private_orders_get**](TradeApi.md#private_orders_get) | **GET** /private/orders | 
[**private_orders_post**](TradeApi.md#private_orders_post) | **POST** /private/orders | 
[**private_trades_get**](TradeApi.md#private_trades_get) | **GET** /private/trades | 


# **private_orders_cancel_post**
> PrivateOrdersGet200ResponseInner private_orders_cancel_post(private_orders_cancel_post_request)

Cancel an order

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (signature):
* Basic Authentication (basicAuth):
* Api Key Authentication (sessionToken):
* Api Key Authentication (nonce):

```python
import exapi_client_python
from exapi_client_python.models.private_orders_cancel_post_request import PrivateOrdersCancelPostRequest
from exapi_client_python.models.private_orders_get200_response_inner import PrivateOrdersGet200ResponseInner
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
    api_instance = exapi_client_python.TradeApi(api_client)
    private_orders_cancel_post_request = exapi_client_python.PrivateOrdersCancelPostRequest() # PrivateOrdersCancelPostRequest | 

    try:
        api_response = api_instance.private_orders_cancel_post(private_orders_cancel_post_request)
        print("The response of TradeApi->private_orders_cancel_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->private_orders_cancel_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **private_orders_cancel_post_request** | [**PrivateOrdersCancelPostRequest**](PrivateOrdersCancelPostRequest.md)|  | 

### Return type

[**PrivateOrdersGet200ResponseInner**](PrivateOrdersGet200ResponseInner.md)

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

# **private_orders_get**
> List[PrivateOrdersGet200ResponseInner] private_orders_get(symbol=symbol, is_open=is_open, has_filled=has_filled, side=side, page=page, limit=limit)

Get the user orders

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (signature):
* Basic Authentication (basicAuth):
* Api Key Authentication (sessionToken):
* Api Key Authentication (nonce):

```python
import exapi_client_python
from exapi_client_python.models.private_orders_get200_response_inner import PrivateOrdersGet200ResponseInner
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
    api_instance = exapi_client_python.TradeApi(api_client)
    symbol = 'symbol_example' # str |  (optional)
    is_open = None # object |  (optional)
    has_filled = None # object |  (optional)
    side = 'side_example' # str |  (optional)
    page = 3.4 # float |  (optional)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.private_orders_get(symbol=symbol, is_open=is_open, has_filled=has_filled, side=side, page=page, limit=limit)
        print("The response of TradeApi->private_orders_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->private_orders_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] 
 **is_open** | [**object**](.md)|  | [optional] 
 **has_filled** | [**object**](.md)|  | [optional] 
 **side** | **str**|  | [optional] 
 **page** | **float**|  | [optional] 
 **limit** | **float**|  | [optional] 

### Return type

[**List[PrivateOrdersGet200ResponseInner]**](PrivateOrdersGet200ResponseInner.md)

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

# **private_orders_post**
> PrivateOrdersGet200ResponseInner private_orders_post(private_orders_post_request)

Create a new order

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (signature):
* Basic Authentication (basicAuth):
* Api Key Authentication (sessionToken):
* Api Key Authentication (nonce):

```python
import exapi_client_python
from exapi_client_python.models.private_orders_get200_response_inner import PrivateOrdersGet200ResponseInner
from exapi_client_python.models.private_orders_post_request import PrivateOrdersPostRequest
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
    api_instance = exapi_client_python.TradeApi(api_client)
    private_orders_post_request = exapi_client_python.PrivateOrdersPostRequest() # PrivateOrdersPostRequest | 

    try:
        api_response = api_instance.private_orders_post(private_orders_post_request)
        print("The response of TradeApi->private_orders_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->private_orders_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **private_orders_post_request** | [**PrivateOrdersPostRequest**](PrivateOrdersPostRequest.md)|  | 

### Return type

[**PrivateOrdersGet200ResponseInner**](PrivateOrdersGet200ResponseInner.md)

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

# **private_trades_get**
> List[PrivateTradesGet200ResponseInner] private_trades_get(symbol=symbol, side=side, taker_or_maker=taker_or_maker, page=page, limit=limit)

Get the user trades

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (signature):
* Basic Authentication (basicAuth):
* Api Key Authentication (sessionToken):
* Api Key Authentication (nonce):

```python
import exapi_client_python
from exapi_client_python.models.private_trades_get200_response_inner import PrivateTradesGet200ResponseInner
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
    api_instance = exapi_client_python.TradeApi(api_client)
    symbol = 'symbol_example' # str |  (optional)
    side = 'side_example' # str |  (optional)
    taker_or_maker = 'taker_or_maker_example' # str |  (optional)
    page = 3.4 # float |  (optional)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.private_trades_get(symbol=symbol, side=side, taker_or_maker=taker_or_maker, page=page, limit=limit)
        print("The response of TradeApi->private_trades_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradeApi->private_trades_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] 
 **side** | **str**|  | [optional] 
 **taker_or_maker** | **str**|  | [optional] 
 **page** | **float**|  | [optional] 
 **limit** | **float**|  | [optional] 

### Return type

[**List[PrivateTradesGet200ResponseInner]**](PrivateTradesGet200ResponseInner.md)

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

