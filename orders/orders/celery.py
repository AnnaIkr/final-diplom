import os

import celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orders")

app = celery.Celery("orders")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()