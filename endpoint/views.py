from django.http import JsonResponse, HttpResponseBadRequest
from static import parse
import geopy.distance


def api_req(request):
    # Only allow GET requests
    if request.method == 'GET':

        for inv_hash in parse.INVALID_HASHES:
            print(inv_hash['blurhash'], inv_hash['name'])

        # If no restaurants meet criteria, empty json object is returned
        ret = {'restaurants': []}

        # Get the json data from parse.py
        restaurants = parse.DATA

        # Get queary parameters
        queary = request.GET.get('q', None).lower()
        lat = request.GET.get('lat', None)
        lon = request.GET.get('lon', None)

        # Return 400 if queary parameters are not correct
        if not queary or not lat or not lon:
            return HttpResponseBadRequest('Invalid search parameters')

        # This a list where the restaurants that match q parameter are stored
        matched = []

        # Search for q in the name, tags and description
        # search terms and targets are decapitalized to get better results
        # Full and partial matches are accepted
        for location in restaurants['restaurants']:
            if (queary in location['name'].lower() or
                    queary in [tag.lower() for tag in location['tags']] or
                    queary in location['description'].lower()):
                matched.append(location)

        #  Distance is calculated only for restaurants with q because it is more
        # expencive operation
        for item in matched:
            dist = geopy.distance.vincenty(
                (item['location'][1], item['location'][0]),
                (float(lat), float(lon))
            ).km
            if dist < 3:
                ret['restaurants'].append(item)

        # Found restaurants are returned in json object
        return JsonResponse(ret, json_dumps_params={'indent': 2})
    else:

        # Only GET requests are allowed
        return HttpResponseBadRequest('Invalid request')
