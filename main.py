import datapoint
import os

os.system("clear")
fog = False

conn = datapoint.Manager(api_key="*YOUR_API_KEY*")

site = conn.get_nearest_forecast_site(55.94886, -3.19910)
print("For " + site.name + ",")

forecast = conn.get_forecast_for_site(site.id, "3hourly")

for timestep in forecast.days[0].timesteps:
    if timestep.humidity.value >= 50 and timestep.temperature.value <= 5:
        fog = True

if fog == True:
    print("looks like you'll need to defrost your windscreen!")
else:
    print("don't worry. You don't need to defrost your windscreen today :)")