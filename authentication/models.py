from django.db import models
import uuid
from django.db import transaction


class VisitorCount(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    count = models.IntegerField(default=0)

    @classmethod
    def increment(cls):
        with transaction.atomic():
            obj = cls.objects.select_for_update().first()
            obj.count += 1
            obj.save()

        return obj

    @classmethod
    def reset(cls):
        with transaction.atomic():
            obj = cls.objects.select_for_update().first()
            obj.count = 0
            obj.save()

        return obj
