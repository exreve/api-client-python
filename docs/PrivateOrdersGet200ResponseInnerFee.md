# PrivateOrdersGet200ResponseInnerFee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | 
**cost** | **str** |  | 
**rate** | **str** |  | 

## Example

```python
from exapi_client_python.models.private_orders_get200_response_inner_fee import PrivateOrdersGet200ResponseInnerFee

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateOrdersGet200ResponseInnerFee from a JSON string
private_orders_get200_response_inner_fee_instance = PrivateOrdersGet200ResponseInnerFee.from_json(json)
# print the JSON string representation of the object
print(PrivateOrdersGet200ResponseInnerFee.to_json())

# convert the object into a dict
private_orders_get200_response_inner_fee_dict = private_orders_get200_response_inner_fee_instance.to_dict()
# create an instance of PrivateOrdersGet200ResponseInnerFee from a dict
private_orders_get200_response_inner_fee_from_dict = PrivateOrdersGet200ResponseInnerFee.from_dict(private_orders_get200_response_inner_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


