import datetime
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FieldWorker
from .serializers import FieldWorkerSerializer, GetFieldWorkerSerializer


class WorkerListApiView(APIView):

    # 1. List all
    def get(self, request, *args, **kwargs):
        """
        List all the worker items for given requested user
        """
        workers = FieldWorker.objects.all()
        serializer = GetFieldWorkerSerializer(workers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        """
        Create the Worker with given worker data
        """
        data = {
            "first_name": request.data.get('first_name'),
            "last_name": request.data.get('last_name'),
            "function": request.data.get('function') if request.data.get('function') else 'Other',
            "created_at": datetime.datetime.now(tz=timezone.utc),
            "updated_at": datetime.datetime.now(tz=timezone.utc)
        }
        serializer = FieldWorkerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkerDetailApiView(APIView):

    def get_object(self, worker_id):
        """
        Helper method to get the object with given worker_id, and user_id
        """
        try:
            return FieldWorker.objects.get(id=worker_id)
        except FieldWorker.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, worker_id, *args, **kwargs):
        """
        Retrieves the Worker with given worker_id
        """
        worker_instance = self.get_object(worker_id)
        if not worker_instance:
            return Response(
                {"response": "Object with worker id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = GetFieldWorkerSerializer(worker_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def patch(self, request, worker_id, *args, **kwargs):
        """
        Updates the worker item with given worker_id if exists
        """
        worker_instance = self.get_object(worker_id)
        if not worker_instance:
            return Response(
                {"response": "Object with worker id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            "first_name": request.data.get('first_name'),
            "last_name": request.data.get('last_name'),
            "function": request.data.get('function'),
            "updated_at": datetime.datetime.now(tz=timezone.utc)
        }
        serializer = FieldWorkerSerializer(instance=worker_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, worker_id, *args, **kwargs):
        """
        Deletes the worker item with given worker_id if exists
        """
        worker_instance = self.get_object(worker_id)
        if not worker_instance:
            return Response(
                {"response": "Object with worker id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        worker_instance.delete()
        return Response(
            {"response": "Object deleted!"},
            status=status.HTTP_200_OK
        )