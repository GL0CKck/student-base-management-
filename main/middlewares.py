from .models import SubGroup


def group_context_processor(request):
    context = {}
    context['group'] = SubGroup.objects.all()
    return context
