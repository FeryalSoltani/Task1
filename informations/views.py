
from rest_framework import generics, viewsets
from rest_framework.parsers import FormParser, JSONParser
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Data
from .serializers import DataSerializer


class DataList(generics.ListAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer


class DataDetail(generics.RetrieveAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer


class DataCRUDViewSet(viewsets.ModelViewSet):
    parser_classes = [FormParser, JSONParser]
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = DataSerializer
