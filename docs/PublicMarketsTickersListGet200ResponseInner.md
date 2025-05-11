# PublicMarketsTickersListGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** |  | 
**last_price** | **str** |  | 
**price_change_percent** | **str** |  | 
**base_volume** | **str** |  | 

## Example

```python
from exapi_client_python.models.public_markets_tickers_list_get200_response_inner import PublicMarketsTickersListGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of PublicMarketsTickersListGet200ResponseInner from a JSON string
public_markets_tickers_list_get200_response_inner_instance = PublicMarketsTickersListGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(PublicMarketsTickersListGet200ResponseInner.to_json())

# convert the object into a dict
public_markets_tickers_list_get200_response_inner_dict = public_markets_tickers_list_get200_response_inner_instance.to_dict()
# create an instance of PublicMarketsTickersListGet200ResponseInner from a dict
public_markets_tickers_list_get200_response_inner_from_dict = PublicMarketsTickersListGet200ResponseInner.from_dict(public_markets_tickers_list_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


