# -*- coding: utf-8 -*-
import os
import django

#  you have to set the correct path to you settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.local")
django.setup()


from project.apps.bla.models import MyModel


def run():
    # do the work
    m = MyModel.objects.get(pk=1)


if __name__ == '__main__':
    run()