from django.http import HttpResponse, JsonResponse
from tasks.models import Task
from django.core import serializers
from rest_framework.response import Response
from tasks.serializer import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

@api_view(["GET"])
def get_tasks(request):
    task = Task.objects.all()
    task_json = serializers.serialize("json", task)
    return HttpResponse(task_json, content_type="application/json")


@api_view(["POST"])
def post_Task(request):
    print(request)
    infoJson = JSONParser().parse(request)
    print(infoJson)
    serializer_class = TaskSerializer(data=infoJson)
    if serializer_class.is_valid():
        serializer_class.save()
        return JsonResponse(serializer_class.data, status=201)
    return JsonResponse(serializer_class.errors, status=400)


@api_view(["DELETE"])
def delete_tasks(request):
    Task.objects.all().delete()
    return Response({"Deletet All tasks"})