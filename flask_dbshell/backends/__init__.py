import subprocess


def load_backend(dburl):
    if dburl.backend is None:
        raise ValueError('database backend is not specified')
    module_name = dburl.backend
    class_name = dburl.backend.capitalize() + 'Backend'
    try:
        module = __import__(module_name, globals(), locals())
    except ImportError as e:
        raise UnknownBackendError('Unknown backend: "%s"' % dburl.backend)
    backend_cls = getattr(module, class_name)
    return backend_cls(dburl)


class UnknownBackendError(Exception):
    pass


class BackendOptionError(Exception):
    pass


class BaseBackend(object):

    def __init__(self, dburl):
        self._dburl = dburl

    def compile_command(self):
        raise NotImplementedError

    def run_shell(self):
        command = self.compile_command()
        self.execute_command(command)

    def execute_command(self, command):
        subprocess.call(command)
