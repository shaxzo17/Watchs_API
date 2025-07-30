from functools import partial
import mixins
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import mixins , status
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Watch
from .serializers import WatchSerializer


# # with mixins

# class WatchListCreateView(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset = Watch.objects.all()
#     serializer_class = WatchSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request , *args , **kwargs)
#
#     def post(self, request):
#         return self.create(request)
#
#
# class WatchDetailView(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     queryset = Watch.objects.all()
#     serializer_class = WatchSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args , **kwargs):
#         return self.update(request , *args , **kwargs)
#
#     def delete(self, request, *args , **kwargs):
#         return self.destroy(request, *args , **kwargs)

# #without mixins

# class WatchListCreateView(GenericAPIView):
#     queryset = Watch.objects.all()
#     serializer_class = WatchSerializer
#
#     def get(self, request):
#         watches = self.get_queryset()
#         serializer = self.get_serializer(watches, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class WatchDelView(GenericAPIView):
#     queryset = Watch.objects.all()
#     serializer_class = WatchSerializer
#
#     def get_object(self, pk):
#         try:
#             return Watch.objects.get(pk=pk)
#         except Watch.DoesNotExist:
#             return None
#
#     def get(self, request, pk):
#         watch = self.get_object(pk)
#         if not watch:
#             return Response({'error': 'Watch not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = self.get_serializer(watch)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         watch = self.get_object(pk)
#         if not watch:
#             return Response({'error': 'Watch not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = self.get_serializer(watch, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def patch(self, request, pk):
#         watch = self.get_object(pk)
#         if not watch:
#             return Response({'error': 'Watch not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = self.get_serializer(watch, data=request.data , partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#     def delete(self, request, pk):
#         watch = self.get_object(pk)
#         if not watch:
#             return Response({'error': 'Watch not found'}, status=status.HTTP_404_NOT_FOUND)
#         watch.delete()
#         return Response({'message': 'Watch deleted'}, status=status.HTTP_204_NO_CONTENT)

#  #with ViewSet

class WatchViewSet(ModelViewSet):
    queryset = Watch.objects.all()
    serializer_class = WatchSerializer
