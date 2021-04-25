
<h1>httptest documentation</h1>

This document provides information about the usage of *httptest* tool.

**Please, read it carefully before using the tool or opening GitHub issues.**

# Installation



# Usage

## Configuration file

The entire tool is based on a JSON configuration file.
This file contains:
- information about the user package
- the HTTP requests to be executed

To generate the file run:
>httptest init

This command creates the JSON file in the root directory (where the user run the init command) with the default name of `httptest.json` and the following structure:
```json
{
	"package": {
		"name": "package-name",
		"author": "author",
		"description": "package-description"
	},
	"requests": [

	]
}
```

These are the default parameters strictly necessary for the correct functioning of the tool. The user can customize it adding new information.

## Requests

The previous described JSON file contains also the HTTP requests to be tested.
Evey HTTP request has the following structure

```json
{
	"title": "request title",
	"url": "http://google.com",
	"method": "GET",
	"headers": {
		"field": "value"
	},
	"body": {
		"field": "value"
	},
	"expected-status": 200
}

```
The user can give a name to every request with the *title* field. The *expected-status* field contains the HTTP status code that the user expects to be returned in the response.
And of course a GET request won't have the body dictionary.

## Testing

Once the JSON config file is ready, run all the requests typing
>http run

You can specify various options:
- config: specify the configuration file path. By default is set to `httpconfig.json`
- output: specify the output file path. By default is set to `httpoutput.json`

Here's an example:
`httptest run --config ../tests/config.json --output ./output.json`


   
