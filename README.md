NOTE: This is a user-maintained extension of the [pymed](https://pypi.org/project/pymed/) project which was [archived in 2020](https://github.com/gijswobben/pymed). Some bugs in `pymed` are fixed here. This package can be installed via `pip install pymed-paperscraper` since I forked it to support [`paperscraper`](https://github.com/jannisborn/paperscraper).

[![License:
MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/pymed_paperscraper.svg)](https://badge.fury.io/py/pymed_paperscraper)
[![Downloads](https://static.pepy.tech/badge/pymed_paperscraper)](https://pepy.tech/project/pymed_paperscraper)
[![Downloads](https://static.pepy.tech/badge/pymed_paperscraper/month)](https://pepy.tech/project/pymed_paperscraper)

# PyMed - PubMed Access through Python
PyMed is a Python library that provides access to PubMed through the PubMed API.

## Why this library?
The PubMed API is not very well documented and querying it in a performant way is too complicated and time consuming for researchers. This wrapper provides access to the API in a consistent, readable and performant way.

## Features
This library takes care of the following for you:

- Querying the PubMed database (with the standard PubMed query language)
- Batching of requests for better performance
- Parsing and cleaning of the retrieved articles

## Examples
For full (working) examples have a look at the `examples/` folder in this repository. In essence you only need to import the `PubMed` class, instantiate it, and use it to query:

```python
from pymed_paperscraper import PubMed
pubmed = PubMed(tool="MyTool", email="my@email.address")
results = pubmed.query("Some query", max_results=500)
```

## Notes on the API
The original documentation of the PubMed API can be found here: [PubMed Central](https://www.ncbi.nlm.nih.gov/pmc/tools/developers/). PubMed Central kindly requests you to:

> - Do not make concurrent requests, even at off-peak times; and
> - Include two parameters that help to identify your service or application to our servers
>   * _tool_ should be the name of the application, as a string value with no internal spaces, and
>   * _email_ should be the e-mail address of the maintainer of the tool, and should be a valid e-mail address.
