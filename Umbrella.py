import datapoint
import os

os.system("clear")
rain = False

conn = datapoint.Manager(api_key="651a57b2-8d95-4d67-800c-c99dc33ef997")

site = conn.get_nearest_forecast_site(55.94886, -3.19910)
print("For " + site.name + ",")

forecast = conn.get_forecast_for_site(site.id, "3hourly")

for timestep in forecast.days[0].timesteps:
    if timestep.precipitation.value >= 50:
        fog = True

if fog == True:
    print("looks like you'll need an umbrella today!")
else:
    print("don't worry. You can forget the umbrella :)")