from . import BaseBackend


class MysqlBackend(BaseBackend):

    def compile_command(self):
        parts = []
        parts.append('mysql')
        if self._dburl.host:
            parts.append('--host=%s' % self._dburl.host)
        if self._dburl.port:
            parts.append('--port=%s' % self._dburl.port)
        if self._dburl.password:
            parts.append('--password=%s' % self._dburl.password)
        if self._dburl.user:
            parts.append('--user=%s' % self._dburl.user)

        if self._dburl.database is not None:
            parts.append(self._dburl.database)

        return parts
