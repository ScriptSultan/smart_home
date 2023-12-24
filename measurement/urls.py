from django.urls import path


from measurement.views import Sensor, SensorUpdate, Measurement, Sensors_all, Sensor_detail

urlpatterns = [
    path('api/sensors/', Sensor.as_view()),
    path('api/sensors/<pk>', SensorUpdate.as_view()),
    path('api/measurement/', Measurement.as_view()),
    path('api/sensors/', Sensors_all.as_view()),
    path('api/measurements/', Sensor_detail.as_view()),
]
