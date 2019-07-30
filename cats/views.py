import json
from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from .models import Cat

# Create your views here.


def catsList(request):
    cats = Cat.objects.order_by('created_date').all()
    data = serialize('json', cats)
    response = {
        'statusCode': 200,
        'message': 'Fetched list of cats', 'data': data
    }
    return JsonResponse(response)


def catRemoveById(parameter_list, cat_id):
    c = Cat.objects.get(pk=cat_id)
    # This will delete the Cat with matching pk
    c.delete()
    response = {'statusCode': 404, 'message': 'Removed cat'}
    return JsonResponse(response)


def catById(parameter_list, cat_id):
    cat = Cat.objects.get(pk=cat_id)
    if cat:
        response = {
            'statusCode': 200,
            'message': 'Fetched list of cats by parameter', 'data': {
                'catId': cat.id,
                'catName': cat.name,
                'catAge': cat.age,
                'catBreed': cat.breed,
                'createdAt': cat.created_date
            }
        }
    else:
        response = {'statusCode': 404, 'message': 'Not found this cat'}

    return JsonResponse(response)


@csrf_exempt
def createCat(request):
    if request.method == 'POST':
        name = request.POST.get("name", "")
        breed = request.POST.get("breed", "")
        gender = request.POST.get("gender", "")
        age = request.POST.get("age", "")

        cat = Cat.objects.create(
            name=name, breed=breed, gender=gender, age=age)
        response = {'statusCode': 201,
                    'message': 'Created a cat', 'data': {
                        'id': cat.id,
                        'name': cat.name,
                        'createdAt': cat.created_date
                    }}
    else:
        response = {'statusCode': 406, 'message': 'Accepts only post method'}

    return JsonResponse(response)
