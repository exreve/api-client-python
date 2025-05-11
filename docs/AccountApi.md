# exapi_client_python.AccountApi

All URIs are relative to *https://api.exkoin.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**private_balances_get**](AccountApi.md#private_balances_get) | **GET** /private/balances | 
[**private_deposit_address_get**](AccountApi.md#private_deposit_address_get) | **GET** /private/deposit-address | 
[**private_deposits_get**](AccountApi.md#private_deposits_get) | **GET** /private/deposits | 
[**private_withdrawal_get**](AccountApi.md#private_withdrawal_get) | **GET** /private/withdrawal | 
[**private_withdrawals_detail_get**](AccountApi.md#private_withdrawals_detail_get) | **GET** /private/withdrawals/detail | 
[**private_withdrawals_finish_post**](AccountApi.md#private_withdrawals_finish_post) | **POST** /private/withdrawals/finish | 
[**private_withdrawals_get**](AccountApi.md#private_withdrawals_get) | **GET** /private/withdrawals | 
[**private_withdrawals_prepare_post**](AccountApi.md#private_withdrawals_prepare_post) | **POST** /private/withdrawals/prepare | 


# **private_balances_get**
> PrivateBalancesGet200Response private_balances_get()

Get the user balances

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (signature):
* Basic Authentication (basicAuth):
* Api Key Authentication (sessionToken):
* Api Key Authentication (nonce):

```python
import exapi_client_python
from exapi_client_python.models.private_balances_get200_response import PrivateBalancesGet200Response
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
    api_instance = exapi_client_python.AccountApi(api_client)

    try:
        api_response = api_instance.private_balances_get()
        print("The response of AccountApi->private_balances_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->private_balances_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PrivateBalancesGet200Response**](PrivateBalancesGet200Response.md)

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

# **private_deposit_address_get**
> PrivateDepositAddressGet200Response private_deposit_address_get(network, currency)

Get a deposit address and informations for a currency/network pair

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (signature):
* Basic Authentication (basicAuth):
* Api Key Authentication (sessionToken):
* Api Key Authentication (nonce):

```python
import exapi_client_python
from exapi_client_python.models.private_deposit_address_get200_response import PrivateDepositAddressGet200Response
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
    api_instance = exapi_client_python.AccountApi(api_client)
    network = 'network_example' # str | 
    currency = 'currency_example' # str | 

    try:
        api_response = api_instance.private_deposit_address_get(network, currency)
        print("The response of AccountApi->private_deposit_address_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->private_deposit_address_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | **str**|  | 
 **currency** | **str**|  | 

### Return type

[**PrivateDepositAddressGet200Response**](PrivateDepositAddressGet200Response.md)

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

# **private_deposits_get**
> List[PrivateDepositsGet200ResponseInner] private_deposits_get(currency=currency, network=network, status=status, limit=limit, page=page, start_time=start_time, end_time=end_time)

Get the user deposits

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (signature):
* Basic Authentication (basicAuth):
* Api Key Authentication (sessionToken):
* Api Key Authentication (nonce):

```python
import exapi_client_python
from exapi_client_python.models.private_deposits_get200_response_inner import PrivateDepositsGet200ResponseInner
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
    api_instance = exapi_client_python.AccountApi(api_client)
    currency = 'currency_example' # str |  (optional)
    network = 'network_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    limit = 3.4 # float |  (optional)
    page = 3.4 # float |  (optional)
    start_time = 3.4 # float |  (optional)
    end_time = 3.4 # float |  (optional)

    try:
        api_response = api_instance.private_deposits_get(currency=currency, network=network, status=status, limit=limit, page=page, start_time=start_time, end_time=end_time)
        print("The response of AccountApi->private_deposits_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->private_deposits_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**|  | [optional] 
 **network** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **limit** | **float**|  | [optional] 
 **page** | **float**|  | [optional] 
 **start_time** | **float**|  | [optional] 
 **end_time** | **float**|  | [optional] 

### Return type

[**List[PrivateDepositsGet200ResponseInner]**](PrivateDepositsGet200ResponseInner.md)

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

# **private_withdrawal_get**
> PrivateWithdrawalsFinishPost200Response private_withdrawal_get(id)

Get a specific withdrawal

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (signature):
* Basic Authentication (basicAuth):
* Api Key Authentication (sessionToken):
* Api Key Authentication (nonce):

```python
import exapi_client_python
from exapi_client_python.models.private_withdrawals_finish_post200_response import PrivateWithdrawalsFinishPost200Response
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
    api_instance = exapi_client_python.AccountApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.private_withdrawal_get(id)
        print("The response of AccountApi->private_withdrawal_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->private_withdrawal_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PrivateWithdrawalsFinishPost200Response**](PrivateWithdrawalsFinishPost200Response.md)

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

# **private_withdrawals_detail_get**
> PrivateWithdrawalsDetailGet200Response private_withdrawals_detail_get(currency, network)

Get the withdrawal details for a currency/network pair

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (signature):
* Basic Authentication (basicAuth):
* Api Key Authentication (sessionToken):
* Api Key Authentication (nonce):

```python
import exapi_client_python
from exapi_client_python.models.private_withdrawals_detail_get200_response import PrivateWithdrawalsDetailGet200Response
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
    api_instance = exapi_client_python.AccountApi(api_client)
    currency = 'currency_example' # str | 
    network = 'network_example' # str | 

    try:
        api_response = api_instance.private_withdrawals_detail_get(currency, network)
        print("The response of AccountApi->private_withdrawals_detail_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->private_withdrawals_detail_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**|  | 
 **network** | **str**|  | 

### Return type

[**PrivateWithdrawalsDetailGet200Response**](PrivateWithdrawalsDetailGet200Response.md)

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

# **private_withdrawals_finish_post**
> PrivateWithdrawalsFinishPost200Response private_withdrawals_finish_post(private_withdrawals_finish_post_request)

Finish a withdrawal (use the payload from prepare-withdraw)

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (signature):
* Basic Authentication (basicAuth):
* Api Key Authentication (sessionToken):
* Api Key Authentication (nonce):

```python
import exapi_client_python
from exapi_client_python.models.private_withdrawals_finish_post200_response import PrivateWithdrawalsFinishPost200Response
from exapi_client_python.models.private_withdrawals_finish_post_request import PrivateWithdrawalsFinishPostRequest
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
    api_instance = exapi_client_python.AccountApi(api_client)
    private_withdrawals_finish_post_request = exapi_client_python.PrivateWithdrawalsFinishPostRequest() # PrivateWithdrawalsFinishPostRequest | 

    try:
        api_response = api_instance.private_withdrawals_finish_post(private_withdrawals_finish_post_request)
        print("The response of AccountApi->private_withdrawals_finish_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->private_withdrawals_finish_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **private_withdrawals_finish_post_request** | [**PrivateWithdrawalsFinishPostRequest**](PrivateWithdrawalsFinishPostRequest.md)|  | 

### Return type

[**PrivateWithdrawalsFinishPost200Response**](PrivateWithdrawalsFinishPost200Response.md)

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

# **private_withdrawals_get**
> List[PrivateWithdrawalsFinishPost200Response] private_withdrawals_get(currency=currency, network=network, limit=limit, status=status, page=page, start_time=start_time, end_time=end_time)

Get the user withdrawals

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (signature):
* Basic Authentication (basicAuth):
* Api Key Authentication (sessionToken):
* Api Key Authentication (nonce):

```python
import exapi_client_python
from exapi_client_python.models.private_withdrawals_finish_post200_response import PrivateWithdrawalsFinishPost200Response
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
    api_instance = exapi_client_python.AccountApi(api_client)
    currency = 'currency_example' # str |  (optional)
    network = 'network_example' # str |  (optional)
    limit = 3.4 # float |  (optional)
    status = 'status_example' # str |  (optional)
    page = 3.4 # float |  (optional)
    start_time = 3.4 # float |  (optional)
    end_time = 3.4 # float |  (optional)

    try:
        api_response = api_instance.private_withdrawals_get(currency=currency, network=network, limit=limit, status=status, page=page, start_time=start_time, end_time=end_time)
        print("The response of AccountApi->private_withdrawals_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->private_withdrawals_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**|  | [optional] 
 **network** | **str**|  | [optional] 
 **limit** | **float**|  | [optional] 
 **status** | **str**|  | [optional] 
 **page** | **float**|  | [optional] 
 **start_time** | **float**|  | [optional] 
 **end_time** | **float**|  | [optional] 

### Return type

[**List[PrivateWithdrawalsFinishPost200Response]**](PrivateWithdrawalsFinishPost200Response.md)

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

# **private_withdrawals_prepare_post**
> PrivateWithdrawalsPreparePost200Response private_withdrawals_prepare_post(private_withdrawals_prepare_post_request)

Prepare a withdrawal, then you need to call withdraw-finish with the payload

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (signature):
* Basic Authentication (basicAuth):
* Api Key Authentication (sessionToken):
* Api Key Authentication (nonce):

```python
import exapi_client_python
from exapi_client_python.models.private_withdrawals_prepare_post200_response import PrivateWithdrawalsPreparePost200Response
from exapi_client_python.models.private_withdrawals_prepare_post_request import PrivateWithdrawalsPreparePostRequest
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
    api_instance = exapi_client_python.AccountApi(api_client)
    private_withdrawals_prepare_post_request = exapi_client_python.PrivateWithdrawalsPreparePostRequest() # PrivateWithdrawalsPreparePostRequest | 

    try:
        api_response = api_instance.private_withdrawals_prepare_post(private_withdrawals_prepare_post_request)
        print("The response of AccountApi->private_withdrawals_prepare_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->private_withdrawals_prepare_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **private_withdrawals_prepare_post_request** | [**PrivateWithdrawalsPreparePostRequest**](PrivateWithdrawalsPreparePostRequest.md)|  | 

### Return type

[**PrivateWithdrawalsPreparePost200Response**](PrivateWithdrawalsPreparePost200Response.md)

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

