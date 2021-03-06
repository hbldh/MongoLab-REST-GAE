MongoLab-REST-GAE
=================

A Python REST client for using MongoLab storage in Google App Engine.

There is already an existing Python REST module for MongoLab on GitHub,
[pymongolab](https://github.com/puentesarrin/pymongolab), using the Python module
[requests](http://requests.readthedocs.org/en/latest/).
Google App Engine, however, does not allow the use of anything but the Python standard libraries
[urllib](http://docs.python.org/2/library/urllib.html),
[urllib2](http://docs.python.org/2/library/urllib2.html) and
[httplib](http://docs.python.org/2/library/httplib.html) to make HTTP requests,
in conjunction with their own module.

**MongoLab-REST-GAE** therefore only uses [httplib](http://docs.python.org/2/library/httplib.html),
[urllib](http://docs.python.org/2/library/urllib.html) and the
[json](http://docs.python.org/2/library/json.html) standard modules, simplifying the use
of MongoLab storage for Google App Engine.

