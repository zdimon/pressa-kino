# -*- coding: utf-8 -*-
from fabric.api import *
import os
from contextlib import contextmanager as _contextmanager



env.key_filename = [os.path.join(os.environ['HOME'], '.ssh', 'id_rsa.pub')]  # Локальный путь до файла с ключами
env.user = 'pressa'  # На сервере будем работать из под пользователя "zdimon"
env.project_root = '/home/pressa/sites/kino'  # Путь до каталога проекта (на сервере)
env.activate = 'source /home/pressa/bin/activate'
env.hosts = ['95.163.104.125']
env.port =  22

@_contextmanager
def virtualenv():
    with cd(env.project_root):
        with prefix(env.activate):
            yield




def deploy():
    with virtualenv():
        run('git pull') # Пуляемся из репозитория
        run('pip install -r requirements.txt') # ставим пакеты
        run('pwd')
        run('./manage.py collectstatic --noinput') # Собираем статику
        #run('./manage.py sync_translation_fields --noinput') # Собираем статику
        run('./manage.py migrate')
        #run('./manage.py makemessages -l ru')
        #run('./manage.py compilemessages')
        #run('sudo service uwsgi restart')
        #run('find . -name "*.mo" -print -delete')  # Чистим старые скомпиленные файлы gettext'а
        #run('./manage.py compilemessages')  # Собираем новые файлы gettext'а
        #run('sudo supervisorctl restart all')
