# PublicNetworksGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**active** | **object** |  | [optional] 
**chain_like** | **str** |  | 
**address_regex** | **str** |  | [optional] 
**withdrawal_fee_usd** | **float** |  | 
**min_deposit_usd** | **float** |  | 
**logo_url** | **str** |  | 
**min_confirmations** | **float** |  | 
**memo_support** | **object** |  | [optional] 
**explorer_txid** | **str** |  | 
**explorer_address** | **str** |  | 
**native_currency** | **str** |  | 

## Example

```python
from exapi_client_python.models.public_networks_get200_response_inner import PublicNetworksGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of PublicNetworksGet200ResponseInner from a JSON string
public_networks_get200_response_inner_instance = PublicNetworksGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(PublicNetworksGet200ResponseInner.to_json())

# convert the object into a dict
public_networks_get200_response_inner_dict = public_networks_get200_response_inner_instance.to_dict()
# create an instance of PublicNetworksGet200ResponseInner from a dict
public_networks_get200_response_inner_from_dict = PublicNetworksGet200ResponseInner.from_dict(public_networks_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


