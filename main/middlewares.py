import time

import pytz
from django.utils import timezone

from .base import thread_local
from .models import SubGroup


def group_context_processor(request):
    context = {}
    context['group'] = SubGroup.objects.all()
    return context


class RequestTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        thread_local.path = request.path
        thread_local.sql_count = 0
        thread_local.sql_total = 0
        timestamp = time.monotonic()

        response = self.get_response(request)

        print(f'Продолжительность запроса {request.path} - {time.monotonic() - timestamp:.3f} sec.'
              f'Количество SQL-запросов - {thread_local.sql_count}.')

        thread_local.sql_total = 0
        thread_local.sql_count = 0
        thread_local.path = ''
        return response


class LastRequestUser:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            request.user.last_request = timezone.now().replace(tzinfo=pytz.utc)
            request.user.save()
        response = self.get_response(request)
        return response
