from django.shortcuts import render



class SiteUnderConstructionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('middleware is running!!')
        response = render(request, 'core/under_construction.html')
        return response