"""
WSGI config for jsclearing project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""


import sys
my_path=r'D:\workspace\jsclearing'
if not my_path in sys.path:
    sys.path.append(my_path)
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jsclearing.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
