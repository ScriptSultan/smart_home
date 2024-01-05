# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView, \
    ListAPIView, UpdateAPIView
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import MeasurementSerializer, SensorDetailSerializer, SensorUpdateSerializer


# class Sensor(CreateAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorSerializer
#
#
# class Sensors_all(ListAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorSerializer
#
#
# class SensorUpdate(RetrieveUpdateAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorSerializer
#
#
# class Measurement(CreateAPIView):
#     queryset = Measurement.objects.all()
#     serializer_class = MeasurementSerializer
#
#
# class Sensor_detail(RetrieveAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorDetailSerializer


class GetSensors(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, request):
        serializer = SensorDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Measurement(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateData(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorUpdateSerializer


class GetSensorInstance(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
