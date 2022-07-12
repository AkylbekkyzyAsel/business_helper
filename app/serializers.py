from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Company


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = Company
        fields = ('company_name', 'name', 'email', 'surname', 'password')
        lookup_field = 'company_name'

    def create(self, validated_data):
        password = validated_data.pop('password')
        company = Company(**validated_data)
        # user.password = make_password('password')
        company.set_password(password)
        company.save()
        return company












