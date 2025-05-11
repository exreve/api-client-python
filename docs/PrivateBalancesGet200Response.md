# PrivateBalancesGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**free** | **Dict[str, str]** |  | 
**locked** | **Dict[str, str]** |  | 

## Example

```python
from exapi_client_python.models.private_balances_get200_response import PrivateBalancesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateBalancesGet200Response from a JSON string
private_balances_get200_response_instance = PrivateBalancesGet200Response.from_json(json)
# print the JSON string representation of the object
print(PrivateBalancesGet200Response.to_json())

# convert the object into a dict
private_balances_get200_response_dict = private_balances_get200_response_instance.to_dict()
# create an instance of PrivateBalancesGet200Response from a dict
private_balances_get200_response_from_dict = PrivateBalancesGet200Response.from_dict(private_balances_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


