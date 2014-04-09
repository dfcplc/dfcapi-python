# DFCAPI for Python [![Build Status](https://api.travis-ci.org/dfcplc/dfcapi-python.png)](https://travis-ci.org/dfcplc/dfcapi-python)

The DFC API is a Restful API which has been built to facilitate the ability to Setup/Ammend/Cancel & View Direct Debits with Debit Finance Collections Plc

### Install with Composer
To utilize DFCAPI-Python, install it using pip:

`pip install dfcapi`

After installing the pip package, you can now begin simplifying requests by importing unirest:

`import dfcapi`

## Checking API Credentials

```python
response = dfcapi.checkApiKey('TEST-TEST-TEST-TEST','fee78bd3bf59bfb36238b3f67de0a6ea103de130')
```

<hr>
### Thanks
Thanks go out to:
* [thefosk](https://github.com/thefosk) @ [mashape.com](https://mashape.com) - Unirest Restful Library