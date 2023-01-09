from django.conf import settings


class DemoMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        print(request)
        return response   
