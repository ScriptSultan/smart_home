from rest_framework import serializers

# TODO: опишите необходимые сериализаторы

from rest_framework import serializers

from measurement.models import Sensor, Measurement


class SensorSerializer(serializers.Serializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurementSerializer(serializers.Serializer):
    class Meta:
        model = Measurement
        fields = ['id', 'sensor', 'temperature', 'created_at']
