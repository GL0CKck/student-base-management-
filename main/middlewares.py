from .models import SubGroup
import time
from .base import thread_local


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
              f'Количество SQL-запросов - {thread_local.sql_count}.'
              f'Продолжительность SQL-запросов - {thread_local.sql_total:.3f}.')

        thread_local.sql_total = 0
        thread_local.sql_count = 0
        thread_local.path = ''
        return response
