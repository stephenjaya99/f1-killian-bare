from rest_framework import serializers

from killian.libs.loading import get_model

Example = get_model('example', 'Example')


class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = ('name', 'date_created', 'date_updated')
        read_only_fields = ('date_created', 'date_updated')
