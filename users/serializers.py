from rest_framework.serializers import Serializer
from users.models import RoleUser


class UserSerializer(Serializer):
    class Meta:
        model = RoleUser
        fields = ['id', 'username', 'email', 'is_admin', 'is_moderator']
        read_only_fields = ['id', 'is_admin', 'is_moderator']

    @staticmethod
    def get_is_admin(obj):
        return obj.get('is_admin')

    @staticmethod
    def get_is_moderator(obj):
        return obj.get('is_moderator')