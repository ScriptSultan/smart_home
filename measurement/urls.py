from django.urls import path


from measurement.views import Measurement, GetSensors, GetSensorInstance, UpdateData

# urlpatterns = [
#     path('api/sensors/', Sensor.as_view()),
#     path('api/sensors/<pk>', SensorUpdate.as_view()),
#     path('api/measurement/', Measurement.as_view()),
#     path('api/sensors/', Sensors_all.as_view()),
#     path('api/measurements/', Sensor_detail.as_view()),
# ]


urlpatterns = [
    path("sensors/update/<pk>/", UpdateData.as_view()),
    path("sensors/", GetSensors.as_view()),
    path("sensors/<pk>/", GetSensorInstance.as_view()),
    path("measurements/", Measurement().as_view()),
]