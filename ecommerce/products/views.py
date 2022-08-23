from django.shortcuts import render
from .models import Customer,Products
from rest_framework.decorators import api_view
from rest_framework .views import APIView
from rest_framework.response import Response
from .serializers import CustomerSerializer,ProductSerializer
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
import uuid
# Create your views here.

class CustomerAPIView(generics.GenericAPIView):

    serializer_class = CustomerSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        # serializer.is_valid(raise_exception = True)
        # serializer.save()
        if(serializer.is_valid()):
            serializer.save()
            return Response({
                "RequestId": str(uuid.uuid4()),
                "Message": "User created successfully",
                
                "User": serializer.data}, status=status.HTTP_201_CREATED
                )
        
        return Response({"Errors": serializers.errors}, status=status.HTTP_400_BAD_REQUEST)


        






class ListCategory(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset =Customer.objects.all()
    serializer_class = CustomerSerializer


class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
 
class ListCustomer(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer




class ListProduct(generics.ListCreateAPIView):    
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Products.objects.all()
    serializer_class = ProductSerializer