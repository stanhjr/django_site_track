from django.utils import timezone

from core.models import DateSubscribe


def is_need_subscribe() -> bool:
    date_subscribe = DateSubscribe.objects.last()
    if not date_subscribe:
        return False
    if timezone.now().date() > date_subscribe.date:
        return True
    return False

