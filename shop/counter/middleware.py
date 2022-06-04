from .models import VisitsCounter


class RequestTimeMiddleware:
    """The missleware to count page visits by registered users"""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_anonymous:
            new_item, created = VisitsCounter.objects.get_or_create(path=request.path, user=request.user)

            if not created:
                new_item.counter += 1
            new_item.save()

        response = self.get_response(request)
        return response
