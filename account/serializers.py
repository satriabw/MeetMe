from rest_framework import serializers
from django.contrib.auth.models import User
from account.models import UserProfile, Interest
from rest_framework.validators import UniqueValidator
from django.contrib.auth import password_validation, authenticate
from drf_writable_nested import WritableNestedModelSerializer


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ('id', 'user', 'interest')

class UserProfileSerializer(WritableNestedModelSerializer):
    interest = InterestSerializer(many=True, read_only=True)
    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'sex',
                  'photo', 'phone_number', 'location_lat', 'location_lon',  'interest',
                  'birth_place', 'birth_date', 'created_at', 'updated_at',)
        depth = 3
        read_only_fields = ('id', 'interest',)


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(many=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'profile')
        depth = 2


def field_length(fieldname):
	field = next(field for field in User._meta.fields if field.name == fieldname)
	return field.max_length


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=field_length('username'),
                                      validators=[UniqueValidator(queryset=User.objects.all())], required=True)
    email = serializers.EmailField(max_length=field_length('email'),
                                   validators=[UniqueValidator(queryset=User.objects.all())], required=True)
    password = serializers.CharField(max_length=field_length('password'), required=True)
    first_name = serializers.CharField(max_length=128, required=True)
    last_name = serializers.CharField(max_length=128, required=False)

    def normalize_email(self, email):
        """
        Normalize the email address by lowercasing the domain part of it.
        """
        email = email or ''
        try:
            email_name, domain_part = email.strip().rsplit('@', 1)
        except ValueError:
            pass
        else:
            email = '@'.join([email_name, domain_part.lower()])
        return email

    def validate(self, attrs):
        email = attrs['email']
        password = attrs['password']

        email = self.normalize_email(email)
        if not email:
            raise serializers.ValidationError(
                'Invalid email provided')

        try:
            if User.objects.get(email=email):
                raise serializers.ValidationError(
                    'A user with that email address already exists')
        except User.DoesNotExist:
            pass

        try:
            password_validation.validate_password(password)
        except serializers.ValidationError:
            raise serializers.ValidationError(
                'Invalid password provided')

        return attrs

    def create(self, validated_data):
        email = validated_data['email'].lower()  # set to lower
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name'] if 'first_name' in validated_data else ''
        last_name = validated_data['last_name'] if 'last_name' in validated_data else ''

        user, created = User.objects.get_or_create(username=username, email=email)
        user.set_password(password)

        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name

        user.save()

        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=field_length('email'), required=True)
    password = serializers.CharField(max_length=field_length('password'), required=True)

