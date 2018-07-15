import os
import random
from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run

REPO_URL = 'https://github.com/jeckt/python-tdd-book.git'

def deploy():
    site_folder = '/home/%s/sites/%s' % (env.user, env.host)
    run('mkdir -p %s' % (site_folder,))
    with cd(site_folder):
        _get_latest_source()
        _update_virtualenv()
        _create_or_update_dotenv()
        _update_static_files()
        _update_database()

def _get_latest_source():
    if exists('.git'):
        run('git fetch')
    else:
        run('git clone %s .' % (REPO_URL,))
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run('git reset --hard %s' % (current_commit,))

def _update_virtualenv():
    if not exists('virtualenv/bin/pip'):
        run('python3.6 -m venv virtualenv')
    run('./virtualenv/bin/pip install -r requirements.txt')

def _create_or_update_dotenv():
    append('.env', 'DJANGO_DEBUG_FALSE=y')
    append('.env', 'SITENAME=%s' % (env.host,))
    current_contents = run('cat .env')
    if 'DJANGO_SECRET_KEY' not in current_contents:
        new_secret = ''.join(random.SystemRandom().choices(
            'abcdefghijklmnopqrstuvwxyz0123456789', k=50
        ))
        append('.env', 'DJANGO_SECRET_KEY=%s' % (new_secret,))
    email_password = os.environ['EMAIL_PASSWORD']
    append('.env', 'EMAIL_PASSWORD=%s' %s (email_password,))

def _update_static_files():
    run('./virtualenv/bin/python manage.py collectstatic --noinput')

def _update_database():
    run('./virtualenv/bin/python manage.py migrate --noinput')
