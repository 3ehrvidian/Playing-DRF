from django.http import JsonResponse

def home(request, *args, **kwargs):
    return JsonResponse({"messages": "Hi there, this is your django API responses!"})
