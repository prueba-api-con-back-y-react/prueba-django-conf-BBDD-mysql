from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import *
import json

class PersonView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            persons = list(Person.objects.filter(id=id).values())
            if len(persons) > 0:
                person = persons[0]
                datos = {'message': "Success", 'person': person}
            else:
                datos = {'message': "person not found..."}
            return JsonResponse(datos)
        else:
            persons = list(Person.objects.values())
            if len(persons) > 0:
                datos = {'message': "Success", 'persons': persons}
            else:
                datos = {'message': "persons not found..."}
            return JsonResponse(datos)

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Person.objects.create(name=jd['name'], email=jd['email'], last_name=jd['last_name'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        companies = list(Person.objects.filter(id=id).values())
        if len(companies) > 0:
            company = Person.objects.get(id=id)
            company.name = jd['name']
            company.email = jd['email']
            company.last_name = jd['last_name']
            company.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Person not found..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        persons = list(Person.objects.filter(id=id).values())
        if len(persons) > 0:
            Person.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Person not found..."}
        return JsonResponse(datos)