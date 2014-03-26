from urlparse import urlsplit

from .backends import load_backend


class DbShell(object):

    def __init__(self, **kwargs):
        self._url = DbUrl(**kwargs)

    def run_shell(self):
        backend = load_backend(self._url)
        backend.run_shell()


class DbUrl(object):

    u"""Db url parser

    URL can be specified as a single string,
    like mysql://user:password@host:port/dbname?arg=100
    or explicitly, like DbUrl(host='localhost', port=3456, database='mydb')

    These modes are compatible, so that use can pass both url
    and override some of its parts with explicit arguments.
    I.e, DbUrl(url='mysql://user@host:port/dbname?arg=100', password='123')

    TODO: dialects
    """

    _KNOWN_PARTS = ('backend', 'host', 'port',
                    'database', 'user', 'password')

    def __init__(self, url=None, **kwargs):
        parts = dict()
        if url is not None:
            o = urlsplit(url, allow_fragments=False)
            parts.update(backend=o.scheme or None,
                         database=o.path.lstrip('/') or None,
                         port=o.port,
                         host=o.hostname,
                         password=o.password,
                         user=o.username)
        parts.update(**kwargs)
        # Cleaning dialect specification like
        # mysql+mysqldb://scott:tiger@localhost/foo
        # postgresql+psycopg2://scott:tiger@localhost/mydatabase
        # that is intrinsic to SQLAlchemy db urls
        backend = parts.get('backend', None)
        if (backend is not None
                and '+' in backend):
            parts.update(backend=backend.split('+')[0])
        self._set_parts(**parts)

    def _set_parts(self, **kwargs):
        for key, val in kwargs.iteritems():
            if key not in self._KNOWN_PARTS:
                raise AttributeError('Unknown argument: "%s"' % key)
            setattr(self, key, val)
        for key in set(self._KNOWN_PARTS) - set(kwargs.keys()):
            setattr(self, key, None)
