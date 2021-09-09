from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms.models import model_to_dict
from rest_framework import status
from .models import CarModel


class CarListCreateView(APIView):
    def get(self, *args, **kwargs):
        cars = CarModel.objects.all().values()
        return Response(cars,status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        # print(self.request.data.dict())
        # print(self.request.query_params)
        data = self.request.data.dict()
        car = CarModel.objects.create(**data)
        return Response(model_to_dict(car),status.HTTP_201_CREATED)


class CarRetrieveUpdateDeleteView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = CarModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('Car with this id is not exsist',status.HTTP_404_NOT_FOUND)
        car=CarModel.objects.get(pk=pk)
        return Response(model_to_dict(car),status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = CarModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('Car with this id is not exsist',status.HTTP_404_NOT_FOUND)
        data=self.request.data.dict()
        CarModel.objects.filter(pk=pk).update(**data)
        return Response('Update',status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        return Response('hello form patch')

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = CarModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('Car with this id is not exsist',status.HTTP_404_NOT_FOUND)
        car=CarModel.objects.get(pk=pk)
        car.delete()
        return Response('delete',status.HTTP_204_NO_CONTENT)

# Create
# Retrieve
# Update
# Delete
