from rest_framework import viewsets
from .models import Task  # This must match the class name in models.py
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Create your views here.
