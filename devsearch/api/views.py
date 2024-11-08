from django.http import JsonResponse


def get_routes(request):
    routes = [
        {"GET": "/api/projects/"},
        {"GET": "/api/projects/id"},
        {"POST": "/api/projects/id/vote"},
        {"POST": "/api/users/token"},
        {"POST": "/api/users/token/refresh"},
    ]

    return JsonResponse(routes, safe=False)
