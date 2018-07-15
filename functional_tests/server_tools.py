from fabric.api import run
from fabric.context_managers import settings, shell_env

def _get_manage_dot_py(host):
    return '~/sites/%s/virtualenv/bin/python ~/sites/%s/manage.py' % (host,
                                                                      host)

def reset_database(host):
    manage_dot_py = _get_manage_dot_py(host)
    with settings(host_string='steve@%s' % (host,)):
        run('%s flush --noinput' % manage_dot_py)

def _get_server_env_vars(host):
    env_lines = run('cat ~/sites/%s/.env' % (host,)).splitlines()
    return dict(l.split('=') for l in env_lines if l)

def create_session_on_server(host, email):
    manage_dot_py = _get_manage_dot_py(host)
    with settings(host_string='steve@%s' % (host,)):
        env_vars = _get_server_env_vars(host)
        with shell_env(**env_vars):
            session_key = run('%s create_session %s' % (manage_dot_py, email))
            return session_key.strip()
