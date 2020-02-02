# Woltapp backend pre-assignment
This is my solution to the Woltapp backend pre-assignment developed with
Django in order to retain scalability if needed

## Dependencies
* Python3

## Run Django development server
In order to run Django development server first run:  
`pip3 install -r requirements.txt`  
Then run:  
`python3 manage.py runserver`

## Live demo
Live demo of my solution can be found in  
https://woltapp-assignment.herokuapp.com/restaurants/search  

## API
To search from API endpoint append `?q=<search term>&lat=<latitude coordinate>&lon=<longitude coordinate>`
at the end of the url.  
Response will be a json object with restaurants matching your search.
