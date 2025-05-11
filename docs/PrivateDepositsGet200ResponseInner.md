# PrivateDepositsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**currency** | **str** |  | 
**amount** | **str** |  | 
**fee** | **str** |  | 
**address_to** | **str** |  | [optional] 
**address_from** | **str** |  | [optional] 
**network** | **str** |  | 
**memo** | **str** |  | [optional] 
**txid** | **str** |  | [optional] 
**block_height** | **float** |  | [optional] 
**status** | **str** |  | 
**timestamp** | **float** |  | 
**confirmations** | **float** |  | 
**confirmations_required** | **float** |  | 

## Example

```python
from exapi_client_python.models.private_deposits_get200_response_inner import PrivateDepositsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateDepositsGet200ResponseInner from a JSON string
private_deposits_get200_response_inner_instance = PrivateDepositsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(PrivateDepositsGet200ResponseInner.to_json())

# convert the object into a dict
private_deposits_get200_response_inner_dict = private_deposits_get200_response_inner_instance.to_dict()
# create an instance of PrivateDepositsGet200ResponseInner from a dict
private_deposits_get200_response_inner_from_dict = PrivateDepositsGet200ResponseInner.from_dict(private_deposits_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


