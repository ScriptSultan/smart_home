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
        fields = ['id', 'id_sensor', 'temperature', 'created_at']

class SensorDetailSerializer(serializers.Serializer):
    measurements = MeasurementSerializer(read_only=True, many=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
