from django.http import JsonResponse

def get_Routes(request):
    routes = [
        {
            'Endpoint': '/users',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of users'
        },
    ]

    return JsonResponse()
