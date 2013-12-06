MongoLab-REST-GAE
=================

A Python REST client for using MongoLab storage in Google App Engine.

There is a Python REST module for MongoLab, using the Python module
[requests][http://requests.readthedocs.org/en/latest/] present:
[pymongolab][https://github.com/puentesarrin/pymongolab].
Google App Engine, however, does not allow the use of anything but the Python standard libraries
[urllib][], [urllib2][] and [httplib][] to make HTTP requests, in conjunction with their own module. So

**MongoLab-REST-GAE** uses only [httplib][], [urllib][] and the [json][] standard modules, enabling the use
of MongoLab storage for Google App Engine.

