from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from static import parse
import geopy.distance

@api_view(['GET'])
@csrf_exempt
def api_req(request):
    if request.method == 'GET':
        ret = {'restaurants': []}
        restaurants = parse.data
        queary = request.GET.get('q', None).lower()
        lat = request.GET.get('lat', None)
        lon = request.GET.get('lon', None)


        matched = []

        for r in restaurants:
            for location in restaurants[r]:
                if (queary in location['name'].lower() or
                queary in location['tags'] or queary in location['description']):
                    matched.append(location)
        for item in matched:
            dist = geopy.distance.vincenty(
                (item['location'][1], item['location'][0]),
                (float(lat), float(lon))
            ).km
            if dist < 3:
                ret['restaurants'].append(item)
        return JsonResponse(ret, json_dumps_params={'indent': 2})
