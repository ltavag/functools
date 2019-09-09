import functools
import requests


@functools.lru_cache(maxsize=None)
def get_temp_for_zipcode(zipcode):
    r = requests.get(
            'https://weather.cit.api.here.com/weather/1.0/report.json',
            params={
                'product': 'observation',
                'zipcode': zipcode,
                'oneobservation': True,
                'app_id': 'DemoAppId01082013GAL',
                'app_code': 'AJKnXv84fjrb0KIHawS0Tg'
            })

    return r.json()['observations']['location'][0]['observation'][0]['temperature']


ZIP_CODES = [
        44102,  # Ohio City
        44113,  # Cleveland Heights
        11211,  # Brooklyn NY
        94016,  # SF
        55111   # Minneapolis
]

avg_temp = functools.reduce(
    lambda x, y: float(x)+float(y),
    map(get_temp_for_zipcode, ZIP_CODES)
) / len(ZIP_CODES)

print(avg_temp)
