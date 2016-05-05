# -*- coding: utf-8 -*-
import argparse
import sys
import os

__author__ = 'kong90'

APP_DESC = """
flask-admin.py startproject hello
"""


def start_project(project_name):
    """

    :param project_name: str
    :return:
    """
    os.mkdir(project_name)

    os.makedirs(project_name + '/' + project_name)
    os.makedirs(project_name + '/migrations')  # 数据库迁移
    os.makedirs(project_name + '/tests')  # 测试
    os.makedirs(project_name + '/venv')  # 虚拟环境

    os.makedirs('{0}/{1}/templates'.format(project_name, project_name))
    os.makedirs('{0}/{1}/static'.format(project_name, project_name))
    os.makedirs('{0}/{1}/main'.format(project_name, project_name))

    os.mknod('{0}/requirements.txt'.format(project_name))
    os.mknod('{0}/config.py'.format(project_name))
    os.mknod('{0}/manage.py'.format(project_name))

    os.mknod('{0}/tests/__init__.py'.format(project_name))
    os.mknod('{0}/{1}/__init__.py'.format(project_name, project_name))
    os.mknod('{0}/{1}/email.py'.format(project_name, project_name))
    os.mknod('{0}/{1}/models.py'.format(project_name, project_name))
    os.mknod('{0}/{1}/main/__init__.py'.format(project_name, project_name))
    os.mknod('{0}/{1}/main/errors.py'.format(project_name, project_name))
    os.mknod('{0}/{1}/main/forms.py'.format(project_name, project_name))
    os.mknod('{0}/{1}/main/views.py'.format(project_name, project_name))


def start_app(app_name):
    """

    :param app_name: str
    :return:
    """
    os.mkdir(app_name)

    os.makedirs('{0}/templates'.format(app_name))
    os.makedirs('{0}/static'.format(app_name))
    os.makedirs('{0}//main'.format(app_name))

    os.mknod('{0}/__init__.py'.format(app_name))
    os.mknod('{0}/email.py'.format(app_name))
    os.mknod('{0}/models.py'.format(app_name))
    os.mknod('{0}/main/__init__.py'.format(app_name))
    os.mknod('{0}/main/errors.py'.format(app_name))
    os.mknod('{0}/main/forms.py'.format(app_name))
    os.mknod('{0}/main/views.py'.format(app_name))


def main():
    if len(sys.argv) == 1:
        sys.argv.append('--help')
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--startproject', type=str, default='',
                        help="start project")
    parser.add_argument('-a', '--startapp', type=str, default='', help="create a new app")
    args = parser.parse_args()
    if args.startproject:
        start_project(args.startproject)

    if args.startapp:
        start_app(args.startapp)


if __name__ == "__main__":
    main()
