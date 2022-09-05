from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, Pledge
from .serializers import ProjectSerializers, PledgeSerializers, ProjectDetailSerializer, PledgeDetailSerializer
from django.http import Http404
from rest_framework import status, permissions
from .permissions import IsOwnerOrReadOnly


class PledgeList(APIView):
    
    def get(self, request):
        if request.GET.get('project_id'):
            pledges = Pledge.objects.filter(project_id = request.GET.get('project_id'))
        
        else:
            pledges = Pledge.objects.all()
        serializer = PledgeSerializers(pledges, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK
            )


    def post(self, request):
        serializer = PledgeSerializers(data=request.data)
        if serializer.is_valid():
            project = Project.objects.get(pk=serializer.validated_data['project_id'])
            if project.owner == request.user:
                return Response('You cannot pledge to your own project.', status=status.HTTP_401_UNAUTHORIZED
        )
            serializer.save(supporter=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

class PledgeDetail(APIView):


    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def delete(self, request, pk):
        pledge = Pledge.objects.get(pk=pk)
        if pledge.supporter == request.user:
            pledge.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            status=status.HTTP_401_UNAUTHORIZED
        )

    def get_object(self, pk):
        try:
            pledge = Pledge.objects.get(pk=pk)
            self.check_object_permissions(self.request, pledge)
            return pledge
        except Pledge.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        pledges = self.get_object(pk)
        serializer = PledgeDetailSerializer(pledges)
        return Response(serializer.data)



class ProjectList(APIView):


    def get(self,request):
        projects = Project.objects.all()
        serializer = ProjectSerializers(projects, many=True)
        return Response(serializer.data)


    def post(self,request):
        serializer = ProjectSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

class ProjectDetail(APIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def delete(self, request, pk):
        project = Project.objects.get(pk=pk)
        if project.owner == request.user:
            project.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            status=status.HTTP_401_UNAUTHORIZED
        )


    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        project = self.get_object(pk)
        data = request.data
        serializer = ProjectDetailSerializer(
            instance=project,
            data=data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    