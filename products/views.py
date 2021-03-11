from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import status
from django.views.defaults import bad_request
from .models import *
from .serializers import *
from .permissions import IsOwnerOrReadOnly, IsOwner, IsProductOwner

# Create your views here.


#A generic view for listing and creating products, I did override the post function to add the request.FILES to the model Product.image

class ListProductsAPI(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def post(self, request, *args, **kwargs):
        product = Product()
        product.title = request.POST['title']
        product.description = request.POST['description']
        product.image =request.FILES['image']
        product.price = request.POST['price']
        product.quantity = request.POST['quantity']
        product.seller = request.user
        product.save()
        serializer = ProductSerializer(product)
        return Response(serializer.data)

       


# A simple detail view for a single product where you can retrieve , update or delete it
# Note that that the permissions IsOwnerOrReadOnly is a custom permission that I created
# to ensure that only the user who created the product can update or delete it

class DetailProductApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly]


#view for creating or listing products, note that i overrode the get_queryset function
# to get only the orders that the requesting user had orderd
# I also overrode the perform_create function to get save the user in the model as the user who made the request

class OrderListCreateAPI(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user= user)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)




# Simple retrieve update delete view for orders with custom permission that only the user who created the order can perform any of the functionality

class OrderUpdateReytrieveDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsOwner, permissions.IsAuthenticated]


#view for creating or listing a Cart, note that i overrode the get_queryset function
# to get only the Cart that the requesting user had orderd
# I also overrode the perform_create function to get save the user in the model as the user who made the request

class CartListCreate(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user= user)


# Simple retrieve update delete view for cart with custom permission that only the user who created the cart can perform any of the functionality


class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsOwner, permissions.IsAuthenticated]

#view for listing the state of orders of a buyer , note that i overrode the get_queryset function
# to get only the orders that the requesting user had orderd

class OrderStateBuyerList(generics.ListAPIView):
    serializer_class = StateSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        order = OrderState.objects.filter(buyer=self.request.user)
        return order

#view for listing the state of orders of a seller , note that i overrode the get_queryset function
# to get only the orders that the requesting user had orderd

class OrderStateOwnerList(generics.ListAPIView):
    serializer_class = StateSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        order = OrderState.objects.filter(owner=self.request.user)
        return order

# Simple retrieve update delete view for Order detail with custom permission that only the user who owns the product can perform any of the functionality


class OrderStateDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StateSerializer
    permission_classes = [IsProductOwner, permissions.IsAuthenticated]
    queryset = OrderState.objects.all()

# root api view to list all the endpoints
@api_view(['GET'])
def api_root(request, format = None):
    return Response({
        'products': reverse('products', request=request, format= format),
        'orders': reverse('orders', request=request, format= format),
        'cart': reverse('cart', request=request, format= format),
        'states_buyer': reverse('states_buyer', request=request, format= format),
        'states_owner': reverse('states_owner', request=request, format= format),
        'register': reverse('register', request=request, format= format)

    })

# a registration endpoint 
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
