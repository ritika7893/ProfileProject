from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets


class HelloApiView(APIView):
    """Test API View with all HTTP methods"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            "Uses HTTP methods as function names (get, post, put, patch, delete)",
            "Is similar to a traditional Django view",
            "Gives you full control over logic",
        ]
        return Response({"message": "Hello!", "an_apiview": an_apiview})

    def post(self, request):
        """Create a hello message with your name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}!"
            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object completely"""
        return Response(
            {"method": "PUT", "message": "This would fully update an object."}
        )

    def patch(self, request, pk=None):
        """Handle updating part of an object"""
        return Response(
            {"method": "PATCH", "message": "This would partially update an object."}
        )

    def delete(self, request, pk=None):
        """Handle deleting an object"""
        return Response({"method": "DELETE", "message": "This would delete an object."})


class HelloViewSet(viewsets.ViewSet):
    """Test ViewSet with all CRUD methods"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Handle GET request to list items"""
        viewset_features = [
            "Uses actions like list, create, retrieve, update, partial_update, destroy",
            "Automatically maps to URLs using Routers",
        ]
        return Response(
            {"message": "Hello from ViewSet!", "features": viewset_features}
        )

    def create(self, request):
        """Handle POST request"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            return Response({"message": f"Hello {name}!"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle GET for a single object by ID"""
        return Response({"method": "GET", "id": pk})

    def update(self, request, pk=None):
        """Handle PUT request (full update)"""
        return Response({"method": "PUT", "id": pk})

    def partial_update(self, request, pk=None):
        """Handle PATCH request (partial update)"""
        return Response({"method": "PATCH", "id": pk})

    def destroy(self, request, pk=None):
        """Handle DELETE request"""
        return Response({"method": "DELETE", "id": pk})
