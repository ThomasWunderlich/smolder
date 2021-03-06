Smolder
=======
[![Build Status](https://travis-ci.org/sky-shiny/smolder.svg?branch=master)](https://travis-ci.org/sky-shiny/smolder)

- Smoke test your rest API.
- Validate response times.
- Validate redirects.
- Validate ssl certificates.
- Validate headers.
- More

Installation
============

```
pip install git+git://github.com/sky-shiny/smolder.git
```

Example
=======

```
$> smolder-cli status.github.com examples/github_status.json

Success connecting to status.github.com on port 80
Preparing to execute 2 tests

------------------------------- Github Status -------------------------------
                          http://status.github.com:80/
-----------------------------------------------------------------------------

curl -v -s -o /dev/null -H "User-Agent: Smolder smoke test library"  -X GET \
"http://status.github.com:80/"
Request took 227ms
Status code == 301 and redirect == https://status.github.com/ ........ [PASS]

------------------------------- Github Status -------------------------------
                         https://status.github.com:443/
-----------------------------------------------------------------------------

curl -v -s -o /dev/null -H "User-Agent: Smolder smoke test library"  -X GET \
"https://status.github.com:443/"
Request took 541ms
Status code == 200 ................................................... [PASS]
Body contains "All systems operational" .............................. [PASS]
Response time was 341ms longer than 200ms max (541ms) ................ [FAIL]
FOUND 1 FAILURES IN 4 TESTS
```

Example [Readme](https://github.com/sky-shiny/smolder/blob/master/examples/README.md)

What it does
============

It wraps the "requests" python library inserting headers, authentication etc and
making your requests to a host: provided as a command line argument.

It checks the response from the server for expected status-codes/body/header/dpath-json
contents and passes or fails the test based on definition.

Can be used to specify and pass/fail on performance of api response.

A copy/paste curl equivalent of the request is included in the output for
convenience.

Easily introduced into a CI/CD deploy pipeline.

Without --force, any API requests that are not GET's will be skipped as a safety
mechanism to ensure we're not overwriting or creating data unconsciously.

Checks may be defined in json or yaml documents. See [examples](examples).

Request Options
===============

Request Option | Description
---------------|-------------
name \* | name for the test
protocol \* | tcp, http, https or noop
port \* | 0 - 65535
url | /url/path/to/resource.json
method | GET, POST, PUT, DELETE, OPTION
request_headers (recommended) |  header object to append to requests instansiation.  The host header is probably the most likely requirement.
username | basic auth username
password | basic auth password
cookie | cookie object to append to requests instansiation
data | data for POST or PUT.
file | provide dummy "filename" and dummy "content" as json arguments. Uploads the content as filename to the specified host.
validate_cert | Should we verify the ssl cert when making an https request?  Defaults to False.

*: required

Response Options
================

Response Test Options | Description
----------------------|-----------------------------
response_body_contains | PASS if string in body.
response_body_doesnt_contain | FAIL if string in body.
response_max_time_ms | FAIL if response takes longer than int.
response_json_contains | FAIL if json response at path doesn't match.
expect_status_code | FAIL if response status code differs from int.
response_redirect | FAIL if string not in response location header.
response_headers | FAIL if the headers received from the request doesn't contain the list of headers provided.
response_header_values | FAIL if the *values* of the headers in the test don't match the values in the response.
show_body | output the body to stdout.

Testing
=======
Install smolder from source (from the project root) to get the relevant dependencies:

```pip install . --upgrade```

At the project root run ```nosetests``` to run the tests.

Contributing
============
Contributions welcome.  For the most part, if tests pass and and the request is logical, it will get accepted.  
Please squash your commits into logical units.
Pep8 is encouraged (for the code you write) and a big effort is being made on that regard in v0.2 branch.

Thanks
======

https://github.com/njsaunders

https://github.com/nielsdraaisma

https://github.com/lotia

https://github.com/casibbald
