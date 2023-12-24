# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView, \
    ListAPIView
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer

class Sensor(CreateAPIView):
    queyset = Sensor.objects.all()
    serializer_class = SensorSerializer


class Sensors_all(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorUpdate(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class Measurement(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class Sensor_detail(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer