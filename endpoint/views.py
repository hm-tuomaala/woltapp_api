from django.http import JsonResponse, HttpResponseBadRequest
from static import parse
import geopy.distance


def api_req(request):
    # Only allow GET requests
    if request.method == 'GET':

        ret = {'restaurants': []}
        restaurants = parse.DATA

        queary = request.GET.get('q', None).lower()
        lat = request.GET.get('lat', None)
        lon = request.GET.get('lon', None)

        # Return 400 if search parameters are not correct
        if not queary or not lat or not lon:
            return HttpResponseBadRequest('Invalid search parameters')

        matched = []

        for location in restaurants['restaurants']:
            if (queary in location['name'].lower() or
                    queary in location['tags'] or
                    queary in location['description']):
                matched.append(location)
        for item in matched:
            dist = geopy.distance.vincenty(
                (item['location'][1], item['location'][0]),
                (float(lat), float(lon))
            ).km
            if dist < 3:
                ret['restaurants'].append(item)
        return JsonResponse(ret, json_dumps_params={'indent': 2})
    else:
        return HttpResponseBadRequest('Invalid request')
