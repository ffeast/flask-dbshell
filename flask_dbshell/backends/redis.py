from . import BaseBackend, BackendOptionError


class RedisBackend(BaseBackend):

    def compile_command(self):
        parts = []
        parts.append('redis-cli')
        if self._dburl.host:
            parts.append('-h %s' % self._dburl.host)
        if self._dburl.port:
            parts.append('-p %s' % self._dburl.port)
        if self._dburl.password:
            parts.append('-a %s' % self._dburl.password)
        if self._dburl.user:
            raise BackendOptionError('User is useless for redis')

        if self._dburl.database is not None:
            parts.append('-n %s' % self._dburl.database)

        return parts
