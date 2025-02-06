from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from vps.enums import VPSStatus
from vps.models import VPS

from .serializers import VPSSerializer


class VPSViewSet(
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, GenericViewSet
):
    queryset = VPS.objects.all()
    serializer_class = VPSSerializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = None
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cpu', 'ram', 'hdd', 'status']

    @action(
        detail=True,
        methods=['patch'],
        url_path='change_status',
        url_name='change_status'
    )
    def change_status(self, request, pk=None):
        '''Позволяет изменить статус сервера.'''
        vps = get_object_or_404(VPS, uid=pk)
        new_status = request.data.get('status')

        if new_status not in (status.value for status in VPSStatus):
            return Response(
                {'error': 'Неверный тип статуса.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        vps.status = new_status
        vps.save()
        return Response(
            self.get_serializer(vps).data, status=status.HTTP_200_OK
        )
