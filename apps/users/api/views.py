from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from users.api.serializers import RegistroSerializer

@api_view(['POST',])

def registro_view(request):

    if request.method == 'POST':
        serializer = RegistroSerializer(data= request.data)
        data= {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Se registró correctamente el nuevo usuario"
            data['email'] = user.email
            data['username'] = user.username
        else:
            data= serializer.errors
        return Response(data)