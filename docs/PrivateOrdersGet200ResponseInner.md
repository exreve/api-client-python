# PrivateOrdersGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**client_order_id** | **str** |  | [optional] 
**symbol** | **str** |  | 
**type** | **str** |  | 
**side** | **str** |  | 
**status** | **str** |  | 
**price** | **str** |  | 
**average** | **str** |  | 
**amount** | **str** |  | 
**filled** | **str** |  | 
**remaining** | **str** |  | 
**cost** | **str** |  | 
**fee** | [**PrivateOrdersGet200ResponseInnerFee**](PrivateOrdersGet200ResponseInnerFee.md) |  | 
**created_at** | **float** |  | 
**updated_at** | **float** |  | 

## Example

```python
from exapi_client_python.models.private_orders_get200_response_inner import PrivateOrdersGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateOrdersGet200ResponseInner from a JSON string
private_orders_get200_response_inner_instance = PrivateOrdersGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(PrivateOrdersGet200ResponseInner.to_json())

# convert the object into a dict
private_orders_get200_response_inner_dict = private_orders_get200_response_inner_instance.to_dict()
# create an instance of PrivateOrdersGet200ResponseInner from a dict
private_orders_get200_response_inner_from_dict = PrivateOrdersGet200ResponseInner.from_dict(private_orders_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


