# Allen Institute Mock LIMS implementation

Tested on Python 3.8 with Flask 1.1.2

# Endpoints:

## Fetch Specimen Metadata

`GET` `/specimen_metadata/view`

Returns json metadata of a specimen based on the kind of metadata.

### Query Parameters

|Parameter|Type|Description|
|---|---|---|
|`specimen_id`|`integer`|Unique id property of the Specimen entry in the LIMS that the metadata is associated with|
|`kind`|`string`|The kind of metadata that is to be retrieved (eg. "IVSCC cell locations")|
|`version_number` (opt.)|`integer`|The version of the metadata, which may be defined by the kind of metadata|

### Response

#### Success `200`

```json
{
  "version_number": 2,
  "data": {"foo": "bar"}
}
```

#### Error

|Status Code|Body|
|---|---|
|`500`|`{ "status": 500, "message": "Something went wrong" }`|
|`404`|`{ "status": 404, "message": "Record not found" }`|
|`400`|`{ "status": 400, "message": "Param foo is missing" }`|

### Sample Call

Request:

`GET` `/specimen_metadata/view?specimen_id=1234&kind=IVSCC%20cell%20locations`

Response:

```json
{
  "version_number": 2,
  "data": {"foo": "bar"}
}
```

### Notes

If version_number is not specified, then the current version will be returned

## Store Specimen Metadata

`POST` `/specimen_metadata/store`

Stores json metadata of a specimen based on the kind of metadata.

### URL Params

None. If URL params are provided, the request will be rejected with code 400

### POST body

#### Required:

|Value|Type|Description|
|---|---|---|
|`specimen_id`|`integer`|Unique id property of the Specimen entry in the LIMS that the metadata is associated with|
|`kind`|`string`|The kind of metadata that is to be retrieved (eg. "IVSCC cell locations")|
|`data`|`object`|The metadata to be stored. This should be a vaid JSON object|

#### Example Body:

```json
{
    "specimen_id": 1234,
    "kind": "IVSCC cell locations",
    "data": {"foo": "bar"}
}
```

### Headers

|Header|Value|
|---|---|
|`Content-Type`|`application/json`|

### Response

#### Success `200`

```json
{
  "id": 1234,
  "version_number": 2
}
```

### Error

|Status Code|Body|
|---|---|
|`500`|`{"status": 500, "message": "Something went wrong"}`|
|`404`|`{"status": 404, "message": "Record not found"}`|
|`400`|`{"status": 400, "message": "Param foo is missing"}`|

### Sample Call

Request: 

`POST` `/specimen_metadata/store`

```json
{
  "specimen_id": 1234,
  "kind": "IVSCC cell locations",
  "data": {"foo": "bar"}
}
```

Response: 

```json
{
  "id": 1234,
  "version_number": 2
}
```
