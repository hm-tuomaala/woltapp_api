# Woltapp backend pre-assignment
This is my solution to the Woltapp backend pre-assignment developed with
Django in order to retain scalability if needed

## Dependencies
* Python3

## Run Django development server
_Usage of python's virtualenvironment is advised_
In order to run Django development server first run:  
`pip3 install -r requirements.txt`  
Then run:  
`python3 manage.py runserver`

## Live demo
Live demo of my solution can be found in  
https://woltapp-exercise.herokuapp.com/restaurants/search  

## API
To search from API endpoint append  
`?q={search_term}&lat={latitude_coordinate}&lon={longitude_coordinate}`  
at the end of the url.  
Response will be a json object with restaurants matching your search.  
For example:  
`?q=pizza&lat=60.17045&lon=24.93147`
