from datetime import timedelta

from django.utils import timezone
from rest_framework import permissions
from django.utils.translation import ugettext_lazy as _


class IsUpcoming(permissions.BasePermission):
    message = _('The pickup date is in the past.')

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.date > timezone.now() + timedelta(minutes=1)

class IsPast(permissions.BasePermission):
    message = _('The pickup date is in the future. You only can give feedback to past events.')

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.date < timezone.now() + timedelta(minutes=1)

class IsEmptyPickupDate(permissions.BasePermission):
    message = _('You can only delete empty pickup dates.')

    def has_object_permission(self, request, view, obj):
        return obj.collectors.count() == 0


class HasJoinedPickupDate(permissions.BasePermission):
    message = _('You have not joined this pickup date.')

    def has_object_permission(self, request, view, obj):
        return obj.collectors.filter(id=request.user.id).exists()


class HasNotJoinedPickupDate(permissions.BasePermission):
    message = _('You have already joined this pickup date.')

    def has_object_permission(self, request, view, obj):
        return not obj.collectors.filter(id=request.user.id).exists()


class IsNotFull(permissions.BasePermission):
    message = _('Pickup date is already full.')

    def has_object_permission(self, request, view, obj):
        if not obj.max_collectors:
            return True
        return obj.collectors.count() < obj.max_collectors
