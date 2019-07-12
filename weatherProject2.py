import pyowm
 
owm = pyowm.OWM('44bc6d30578b1f241cb9f46a87d7de3d')
observation = owm.weather_at_place('Ghana,Accra')
w = observation.get_weather()
 
print(w.get_wind())
print(w.get_humidity())






