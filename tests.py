import unittest
from mock import patch

from flask.ext.dbshell import DbUrl, DbShell
from flask.ext.dbshell.backends import BaseBackend, BackendOptionError


class DbUrlTest(unittest.TestCase):

    def test_valid_url(self):
        url = DbUrl('mysql://test:123@dbserver:6666/superdb')
        self.assertEquals(url.backend, 'mysql')
        self.assertEquals(url.user, 'test')
        self.assertEquals(url.password, '123')
        self.assertEquals(url.host, 'dbserver')
        self.assertEquals(url.port, 6666)
        self.assertEquals(url.database, 'superdb')

    def test_url_with_missing_args(self):
        url = DbUrl('mysql://localhost/superdb')
        self.assertEquals(url.backend, 'mysql')
        self.assertEquals(url.user, None)
        self.assertEquals(url.password, None)
        self.assertEquals(url.host, 'localhost')
        self.assertEquals(url.port, None)
        self.assertEquals(url.database, 'superdb')

    def test_explicit_args(self):
        url = DbUrl(backend='mysql', user='test',
                    password='123', host='127.0.0.1',
                    port=8000)
        self.assertEquals(url.backend, 'mysql')
        self.assertEquals(url.user, 'test')
        self.assertEquals(url.password, '123')
        self.assertEquals(url.host, '127.0.0.1')
        self.assertEquals(url.port, 8000)
        self.assertEquals(url.database, None)

    def test_override_args(self):
        url = DbUrl('mysql://test:123@dbserver:6666/superdb',
                    database='anotherdb',
                    password='345')
        self.assertEquals(url.database, 'anotherdb')
        self.assertEquals(url.password, '345')

    def test_unknown_arg(self):
        #with self.assertRaises(AttributeError):
            #DbUrl(unknown_arg=123)
        self.assertRaises(AttributeError,
                          DbUrl,
                          unknown_arg=123)

    def test_backend_with_dialect(self):
        url = DbUrl('mysql+somedialect://user@server/superdb')
        self.assertEquals(url.backend, 'mysql')


class BaseBackendTest(unittest.TestCase):

    @patch.object(BaseBackend, 'execute_command')
    def assert_command(self, dbshell, expected, mock_method):
        dbshell.run_shell()
        mock_method.assert_called_with(expected)


class MysqlBackendTest(BaseBackendTest):

    def test_basic(self):
        self.assert_command(
            DbShell(url='mysql://user:password@127.0.0.1/test'),
            ['mysql',
             '--host=127.0.0.1',
             '--password=password',
             '--user=user',
             'test'])

    def test_simple(self):
        self.assert_command(DbShell(url='mysql:///mydb'),
                            ['mysql', 'mydb'])


class SqliteBackendTest(BaseBackendTest):

    def test_basic(self):
        self.assert_command(
            DbShell(url='sqlite:///dir1/file1'),
            ['sqlite3', 'dir1/file1'])

    def test_unsupported_args(self):
        #with self.assertRaises(BackendOptionError):
        #self.assert_command(DbShell(url='sqlite://127.0.0.1/file'), None)
        self.assertRaises(BackendOptionError,
                          self.assert_command,
                          DbShell(url='sqlite://127.0.0.1/file'),
                          None)


class PostgresqlBackendTest(BaseBackendTest):

    def test_basic(self):
        self.assert_command(
            DbShell(url='postgresql://user:password@127.0.0.1:666/test'),
            ['psql',
             '--host=127.0.0.1',
             '--port=666',
             '--password=password',
             '--username=user',
             'test'])


class RedisBackendTest(BaseBackendTest):

    def test_basic(self):
        self.assert_command(
            DbShell(url='redis://127.0.0.1:3334/redis1', password='pwd'),
            ['redis-cli',
             '-h 127.0.0.1',
             '-p 3334',
             '-a pwd',
             '-n redis1'])

    def test_unsupported_args(self):
        #with self.assertRaises(BackendOptionError):
            #self.assert_command(
                #DbShell(url='redis://user@127.0.0.1:3334/redis1'), None)
        self.assertRaises(BackendOptionError,
                          self.assert_command,
                          DbShell(url='redis://user@127.0.0.1:3334/redis1'),
                          None)


if __name__ == '__main__':
    unittest.main()
