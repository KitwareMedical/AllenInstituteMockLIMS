# lims-mock

Tested on Python 3.8 with Flask 1.1.2

# Endpoints:

## Fetch Specimen Metadata

Returns json metadata of a specimen based on the kind of metadata.

### URL

`/specimen_metadata/view`
 
### Method

`GET`

### URL Params

#### Required

```
specimen_id=[integer] - Unique id property of the Specimen entry in the LIMS that the metadata is associated with
kind=[string] - The kind of metadata that is to be retrieved (eg. "IVSCC cell locations")
```

#### Optional

```
version_number=[integer] - The version of the metadata, which may be defined by the kind of metadata
```

### Success Response

```
Code: 200 - Content: { "version_number": 2, "data": { "foo" : "bar" } }
```

### Error Responses

```
Code: 500 - Content: { "status": 500, "message": "Something went wrong" }
Code: 404 - Content: { "status": 404, "message": "Record not found" }
Code: 400 - Content: { "status": 400, "message": "Param foo is missing" }
message values in the error response are examples
```

### Sample Call

`/specimen_metadata/view?specimen_id=1234&kind=IVSCC%20cell%20locations`

`/specimen_metadata/view?specimen_id=1234&kind=IVSCC%20cell%20locations&version_number=3`

### Notes

```
If version_number is not specified, then the current version will be returned
```

## Store Specimen Metadata

Stores json metadata of a specimen based on the kind of metadata.

### URL

`/specimen_metadata/store`

### Method

`POST`

### URL Params

```
NONE
If URL params are provided, the request will be rejected with code 400
```

### POST body

#### Required:

```
specimen_id=[integer] - Unique id property of the Specimen entry in the LIMS that the metadata is associated with
kind=[string] - The kind of metadata that is to be retrieved (eg. "IVSCC cell locations")
data=[object] - The metadata to be stored - this should be a valid JSON object
```

#### Example Body:

```json
{
    "specimen_id": 1234,
    "kind": "IVSCC cell locations",
    "data": {
        "foo": "bar"
    }
}
```

#### Example Body:

```json
{
    "specimen_id": 1234,
    "kind": "IVSCC expected cell count",
    "data": 2
}
```

### Required Headers

```
Content-Type: application/json
```

### Success Response

```
Code: 200 - Content: { "id": 1234, "version_number": 2 }
```

### Error Responses

```
Code: 500 - Content: { "status": 500, "message": "Something went wrong" }
Code: 404 - Content: { "status": 404, "message": "Record not found" }
Code: 400 - Content: { "status": 400, "message": "Param foo is missing" }
message values in the error response are examples
```

### Sample Call

`/specimen_metadata/store`
