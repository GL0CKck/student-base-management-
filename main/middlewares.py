from .models import SubGroup
import time


def group_context_processor(request):
    context = {}
    context['group'] = SubGroup.objects.all()
    return context


class RequestTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        timestamp = time.monotonic()

        response = self.get_response(request)

        print(f'Продолжительность запроса {request.path} - {time.monotonic() - timestamp:.3f} sec.')

        return response

