# Test Service API
This project is intended as the solution to the Boston Makmur Gemilang Python Developer Backend Test.

This project takes a hands-on look at microservices project with caching mechanism using Python, Flask, Redis and Docker.


## Project Technology Stack
The project itself are built with
* [Python 3.8.5](https://www.python.org/)
* [Flask 2.1.2](https://flask.palletsprojects.com/en/2.1.x/)
* [Flask-Caching 2.0.0](https://flask-caching.readthedocs.io/en/latest/)
* [Redis 4.3.4](https://redis.io/docs/getting-started/)
* [Docker](https://www.docker.com/)

## Microservices Setup and Configuration
To launch the microservices application you will need to perform the following steps below:

### Step 1.
Clone the project directory and navigate to the project directory in your desktop and confirm the presence of the ```docker-compose.yml``` file:
```
git clone https://github.com/RandyBrilliant/bmg-backend-test.git
cd bmg-backend-test
```

### Step 2.
Build each of the microservice Docker container images and launch the microservice environment:
```
docker-compose up -d --build
docker ps
```

### Step 3.
Using your workstations browser - navigate to the following URL to see that the website work as intended:
```
http://localhost:5000/
```

### Step 4.
Using your workstations browser - login, and add products into your cart, and then finally click the checkout option
```
http://localhost:5000/login
```

## Use Case Test API
There will be 2 endpoint where you can request data from the server to get specific data.

### 1. Get Specific Episode.
You can get a specific episode just by `providing partial episode name` on the url.
```
http://localhost:5000/services/{partial-name}
```
For Example:
```
http://localhost:5000/services/one
```
The expected results will be
```
{
  "data": [
    {
      "_links": {
        "self": {
          "href": "https://api.tvmaze.com/episodes/200"
        }
      }, 
      "airdate": "2011-12-18", 
      "airstamp": "2011-12-19T03:00:00+00:00", 
      "airtime": "22:00", 
      "id": 200, 
      "image": {
        "medium": "https://static.tvmaze.com/uploads/images/medium_landscape/5/14589.jpg", 
        "original": "https://static.tvmaze.com/uploads/images/original_untouched/5/14589.jpg"
      }, 
      "name": "Marine One", 
      "number": 12, 
      "rating": {
        "average": 8.5
      }, 
      "runtime": 60, 
      "season": 1, 
      "summary": "<p>In the Season 1 finale, a near-catatonic Carrie is confined to bed as Saul puzzles over the unnerving implications of her time line. Elsewhere, Walker settles on a perch from which to complete his mission; and Brody preps for the vice president's policy summit.</p>", 
      "type": "regular", 
      "url": "https://www.tvmaze.com/episodes/200/homeland-1x12-marine-one"
    }, 
    {
      "_links": {
        "self": {
          "href": "https://api.tvmaze.com/episodes/221"
        }
      }, 
      "airdate": "2013-11-24", 
      "airstamp": "2013-11-25T02:00:00+00:00", 
      "airtime": "21:00", 
      "id": 221, 
      "image": {
        "medium": "https://static.tvmaze.com/uploads/images/medium_landscape/5/14608.jpg", 
        "original": "https://static.tvmaze.com/uploads/images/original_untouched/5/14608.jpg"
      }, 
      "name": "One Last Thing", 
      "number": 9, 
      "rating": {
        "average": 8.1
      }, 
      "runtime": 60, 
      "season": 3, 
      "summary": "<p>Carrie reunites with Brody, but the circumstances are more difficult than either of them imagined. Meanwhile, Saul gets a win from an unlikely source; and Dana struggles with her new life away from home.</p>", 
      "type": "regular", 
      "url": "https://www.tvmaze.com/episodes/221/homeland-3x09-one-last-thing"
    }, 
  ], 
  "message_status": "success", 
  "status_code": 200
}
```

### 2. Update Summary from given Episode ID
You can update the summary from a episode by `specifying the ID` of the episode.
```
PUT http://localhost:5000/services/{id}

header
{
  "Content-Type": "application/json"
}

body request/payload:
{
  "summary": "new summary data"
}
```

For Example:
```
PUT http://localhost:5000/services/189

header
{
  "Content-Type": "application/json"
}

body request/payload:
{
  "summary": "new summary data"
}
```
The expected results will be
```
{
"data": [
{
"_links": {
"self": {
"href": "https://api.tvmaze.com/episodes/189"
}
},
"airdate": "2011-10-02",
"airstamp": "2011-10-03T02:00:00+00:00",
"airtime": "22:00",
"id": 189,
"image": {
"medium": "https://static.tvmaze.com/uploads/images/medium_landscape/5/14578.jpg",
"original": "https://static.tvmaze.com/uploads/images/original_untouched/5/14578.jpg"
},
"name": "Pilot",
"number": 1,
"rating": {
"average": 8.4
},
"runtime": 60,
"season": 1,
"summary": "new summary data",
"type": "regular",
"url": "https://www.tvmaze.com/episodes/189/homeland-1x01-pilot"
}
],
"message_status": "success",
"status_code": 200
}
```
