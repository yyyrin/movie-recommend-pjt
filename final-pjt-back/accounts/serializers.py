from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

class UserSerializer(RegisterSerializer):
    first_name = serializers.CharField()

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['first_name'] = self.validated_data.get('first_name', '')
        print(data)
        return data