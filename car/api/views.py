from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from car.models import Group, Version
from car.api.serializers import GroupSerializer, VersionSerializer

class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Group.objects.all()


class VersionViewSet(viewsets.ModelViewSet):
    serializer_class = VersionSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        queryset = Version.objects.all()
        return queryset
