.. module:: asyncbing

asyncbing API reference
=======================


Searching
=========

.. autofunction:: asyncbing.search

|
.. autoclass:: asyncbing.Search
    :members:

|

.. autoclass:: asyncbing.SearchResponse
    :members:

|
A searchresult represents a search result response from bing (you get it from :class:`asyncbing.SearchResponse`).

.. autoclass:: asyncbing.SearchResult
    :members:

|

Translating
===========

.. autofunction:: asyncbing.translate

|
.. autoclass:: asyncbing.Translate
    :members:

|

.. autoclass:: asyncbing.TranslateResponse
    :members:


|

Exceptions
==========

.. autoclass:: asyncbing.BingException
    :members:

.. autoclass:: asyncbing.BadAuth
    :members:

.. autoclass:: asyncbing.NotEnoughResults
    :members:

.. toctree::
   :maxdepth: 2
   :caption: Contents:

