from . import BaseBackend, BackendOptionError


class SqliteBackend(BaseBackend):

    def compile_command(self):
        parts = []
        parts.append('sqlite3')
        if self._dburl.host:
            raise BackendOptionError('Host is useless for sqlite')
        if self._dburl.port:
            raise BackendOptionError('Port is useless for sqlite')
        if self._dburl.password:
            raise BackendOptionError('Password is useless for sqlite')
        if self._dburl.user:
            raise BackendOptionError('User is useless for sqlite')

        if self._dburl.database is not None:
            parts.append(self._dburl.database)

        return parts
