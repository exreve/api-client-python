# exapi_client_python.PublicApi

All URIs are relative to *https://api.exkoin.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**public_currencies_get**](PublicApi.md#public_currencies_get) | **GET** /public/currencies | 
[**public_exk_config_get**](PublicApi.md#public_exk_config_get) | **GET** /public/exk/config | 
[**public_exk_reserves_get**](PublicApi.md#public_exk_reserves_get) | **GET** /public/exk/reserves | 
[**public_forex_prices_get**](PublicApi.md#public_forex_prices_get) | **GET** /public/forex-prices | 
[**public_funds_transparency_get**](PublicApi.md#public_funds_transparency_get) | **GET** /public/funds-transparency | 
[**public_gains_losses_transparency_get**](PublicApi.md#public_gains_losses_transparency_get) | **GET** /public/gains-losses-transparency | 
[**public_markets_get**](PublicApi.md#public_markets_get) | **GET** /public/markets | 
[**public_markets_tickers_list_get**](PublicApi.md#public_markets_tickers_list_get) | **GET** /public/markets/tickers-list | 
[**public_networks_get**](PublicApi.md#public_networks_get) | **GET** /public/networks | 
[**public_ohlcv_get**](PublicApi.md#public_ohlcv_get) | **GET** /public/ohlcv | 
[**public_orderbook_get**](PublicApi.md#public_orderbook_get) | **GET** /public/orderbook | 
[**public_pools_fees_history_get**](PublicApi.md#public_pools_fees_history_get) | **GET** /public/pools/fees-history | 
[**public_pools_get**](PublicApi.md#public_pools_get) | **GET** /public/pools | 
[**public_trades_get**](PublicApi.md#public_trades_get) | **GET** /public/trades | 


# **public_currencies_get**
> List[PublicCurrenciesGet200ResponseInner] public_currencies_get()

Get all active currencies

### Example


```python
import exapi_client_python
from exapi_client_python.models.public_currencies_get200_response_inner import PublicCurrenciesGet200ResponseInner
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
    api_instance = exapi_client_python.PublicApi(api_client)

    try:
        api_response = api_instance.public_currencies_get()
        print("The response of PublicApi->public_currencies_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->public_currencies_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PublicCurrenciesGet200ResponseInner]**](PublicCurrenciesGet200ResponseInner.md)

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

# **public_exk_config_get**
> PublicExkConfigGet200Response public_exk_config_get()

Get the EXK token configuration

### Example


```python
import exapi_client_python
from exapi_client_python.models.public_exk_config_get200_response import PublicExkConfigGet200Response
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
    api_instance = exapi_client_python.PublicApi(api_client)

    try:
        api_response = api_instance.public_exk_config_get()
        print("The response of PublicApi->public_exk_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->public_exk_config_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PublicExkConfigGet200Response**](PublicExkConfigGet200Response.md)

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

# **public_exk_reserves_get**
> Dict[str, str] public_exk_reserves_get()

Get the EXK reserves

### Example


```python
import exapi_client_python
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
    api_instance = exapi_client_python.PublicApi(api_client)

    try:
        api_response = api_instance.public_exk_reserves_get()
        print("The response of PublicApi->public_exk_reserves_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->public_exk_reserves_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, str]**

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

# **public_forex_prices_get**
> PublicForexPricesGet200Response public_forex_prices_get()

Get the forex prices, base is in USD, eg. EUR, GBP, HKD, SGD, ... Data is from an external provider.

### Example


```python
import exapi_client_python
from exapi_client_python.models.public_forex_prices_get200_response import PublicForexPricesGet200Response
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
    api_instance = exapi_client_python.PublicApi(api_client)

    try:
        api_response = api_instance.public_forex_prices_get()
        print("The response of PublicApi->public_forex_prices_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->public_forex_prices_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PublicForexPricesGet200Response**](PublicForexPricesGet200Response.md)

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

# **public_funds_transparency_get**
> PublicFundsTransparencyGet200Response public_funds_transparency_get()

Get the funds transparency data (overall exchange balances)

### Example


```python
import exapi_client_python
from exapi_client_python.models.public_funds_transparency_get200_response import PublicFundsTransparencyGet200Response
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
    api_instance = exapi_client_python.PublicApi(api_client)

    try:
        api_response = api_instance.public_funds_transparency_get()
        print("The response of PublicApi->public_funds_transparency_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->public_funds_transparency_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PublicFundsTransparencyGet200Response**](PublicFundsTransparencyGet200Response.md)

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

# **public_gains_losses_transparency_get**
> PublicGainsLossesTransparencyGet200Response public_gains_losses_transparency_get(unclaimed_only=unclaimed_only, period=period)

Get transparency information about exchange gains and losses

### Example


```python
import exapi_client_python
from exapi_client_python.models.public_gains_losses_transparency_get200_response import PublicGainsLossesTransparencyGet200Response
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
    api_instance = exapi_client_python.PublicApi(api_client)
    unclaimed_only = None # object |  (optional)
    period = 'period_example' # str |  (optional)

    try:
        api_response = api_instance.public_gains_losses_transparency_get(unclaimed_only=unclaimed_only, period=period)
        print("The response of PublicApi->public_gains_losses_transparency_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->public_gains_losses_transparency_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unclaimed_only** | [**object**](.md)|  | [optional] 
 **period** | **str**|  | [optional] 

### Return type

[**PublicGainsLossesTransparencyGet200Response**](PublicGainsLossesTransparencyGet200Response.md)

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

# **public_markets_get**
> List[PublicMarketsGet200ResponseInner] public_markets_get()

Get all active markets

### Example


```python
import exapi_client_python
from exapi_client_python.models.public_markets_get200_response_inner import PublicMarketsGet200ResponseInner
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
    api_instance = exapi_client_python.PublicApi(api_client)

    try:
        api_response = api_instance.public_markets_get()
        print("The response of PublicApi->public_markets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->public_markets_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PublicMarketsGet200ResponseInner]**](PublicMarketsGet200ResponseInner.md)

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

# **public_markets_tickers_list_get**
> List[PublicMarketsTickersListGet200ResponseInner] public_markets_tickers_list_get()

Get the 24h tickers for all markets

### Example


```python
import exapi_client_python
from exapi_client_python.models.public_markets_tickers_list_get200_response_inner import PublicMarketsTickersListGet200ResponseInner
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
    api_instance = exapi_client_python.PublicApi(api_client)

    try:
        api_response = api_instance.public_markets_tickers_list_get()
        print("The response of PublicApi->public_markets_tickers_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->public_markets_tickers_list_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PublicMarketsTickersListGet200ResponseInner]**](PublicMarketsTickersListGet200ResponseInner.md)

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

# **public_networks_get**
> List[PublicNetworksGet200ResponseInner] public_networks_get()

Get all active networks

### Example


```python
import exapi_client_python
from exapi_client_python.models.public_networks_get200_response_inner import PublicNetworksGet200ResponseInner
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
    api_instance = exapi_client_python.PublicApi(api_client)

    try:
        api_response = api_instance.public_networks_get()
        print("The response of PublicApi->public_networks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->public_networks_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PublicNetworksGet200ResponseInner]**](PublicNetworksGet200ResponseInner.md)

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

# **public_ohlcv_get**
> List[PublicOhlcvGet200ResponseInner] public_ohlcv_get(symbol, interval, page=page, limit=limit)

Get the OHLCV data for a trading pair

### Example


```python
import exapi_client_python
from exapi_client_python.models.public_ohlcv_get200_response_inner import PublicOhlcvGet200ResponseInner
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
    api_instance = exapi_client_python.PublicApi(api_client)
    symbol = 'symbol_example' # str | 
    interval = 3.4 # float | 
    page = 3.4 # float |  (optional)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.public_ohlcv_get(symbol, interval, page=page, limit=limit)
        print("The response of PublicApi->public_ohlcv_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->public_ohlcv_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | 
 **interval** | **float**|  | 
 **page** | **float**|  | [optional] 
 **limit** | **float**|  | [optional] 

### Return type

[**List[PublicOhlcvGet200ResponseInner]**](PublicOhlcvGet200ResponseInner.md)

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

# **public_orderbook_get**
> PublicOrderbookGet200Response public_orderbook_get(symbol)

Get the orderbook for a trading pair

### Example


```python
import exapi_client_python
from exapi_client_python.models.public_orderbook_get200_response import PublicOrderbookGet200Response
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
    api_instance = exapi_client_python.PublicApi(api_client)
    symbol = 'symbol_example' # str | 

    try:
        api_response = api_instance.public_orderbook_get(symbol)
        print("The response of PublicApi->public_orderbook_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->public_orderbook_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | 

### Return type

[**PublicOrderbookGet200Response**](PublicOrderbookGet200Response.md)

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

# **public_pools_fees_history_get**
> List[PublicPoolsFeesHistoryGet200ResponseInner] public_pools_fees_history_get(pool_id=pool_id, start_time=start_time, end_time=end_time, limit=limit, page=page)

Get the pool fees earnings history

### Example


```python
import exapi_client_python
from exapi_client_python.models.public_pools_fees_history_get200_response_inner import PublicPoolsFeesHistoryGet200ResponseInner
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
    api_instance = exapi_client_python.PublicApi(api_client)
    pool_id = 'pool_id_example' # str |  (optional)
    start_time = 3.4 # float |  (optional)
    end_time = 3.4 # float |  (optional)
    limit = 3.4 # float |  (optional)
    page = 3.4 # float |  (optional)

    try:
        api_response = api_instance.public_pools_fees_history_get(pool_id=pool_id, start_time=start_time, end_time=end_time, limit=limit, page=page)
        print("The response of PublicApi->public_pools_fees_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->public_pools_fees_history_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**|  | [optional] 
 **start_time** | **float**|  | [optional] 
 **end_time** | **float**|  | [optional] 
 **limit** | **float**|  | [optional] 
 **page** | **float**|  | [optional] 

### Return type

[**List[PublicPoolsFeesHistoryGet200ResponseInner]**](PublicPoolsFeesHistoryGet200ResponseInner.md)

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
    api_instance = exapi_client_python.PublicApi(api_client)

    try:
        api_response = api_instance.public_pools_get()
        print("The response of PublicApi->public_pools_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->public_pools_get: %s\n" % e)
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

# **public_trades_get**
> List[PublicTradesGet200ResponseInner] public_trades_get(symbol, page=page, limit=limit)

Get the public trades for a trading pair

### Example


```python
import exapi_client_python
from exapi_client_python.models.public_trades_get200_response_inner import PublicTradesGet200ResponseInner
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
    api_instance = exapi_client_python.PublicApi(api_client)
    symbol = 'symbol_example' # str | 
    page = 3.4 # float |  (optional)
    limit = 3.4 # float |  (optional)

    try:
        api_response = api_instance.public_trades_get(symbol, page=page, limit=limit)
        print("The response of PublicApi->public_trades_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->public_trades_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | 
 **page** | **float**|  | [optional] 
 **limit** | **float**|  | [optional] 

### Return type

[**List[PublicTradesGet200ResponseInner]**](PublicTradesGet200ResponseInner.md)

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

