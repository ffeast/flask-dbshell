import subprocess


def load_backend(dburl):

    """Backend loader

    Getting a specified backend name and trying
    to dynamically load the corresponding module.

    To support a new db just create a newdb.py
    containing a "NewdbBackend" class that overrides "compile_command" method
    """

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
