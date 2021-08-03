# suade-challenge

## setting up
Simply clone project. I have containerised the application, so that you can build image and run directly using docker containers.

`docker image build .`

Build Docker image.

`docker container run -p 8000:8000 <docker image id>`

Then you can run it, you should be able to use the web app on localhost:8000 on any web browser.

at which point simply, type in the desired date on: 

`localhost:8000/date/<target-date>`

The date format is: "YYYY-MM-DD", you must give a date that is in the data supplied. 

## How I approached the challenge

### testing
I wrote down how I would manually solve each of the challenge on paper first, this is to clarify the business logic of the application. Thereafter, I initalised some csv files that contain the relevant datafields in each task. I used a TDD approach, whereby each function/feature I added was tested 
on a csv file that I created myself. This is to check that the logic works soundly and also I know exactly which answers I should be expecting. 

This part of the code is stored in suade-challenge/application/tests/unit/

### Building endpoint
Having built all of the functions that would handle the logic, we can thus import it into an endpoint. For the endpoint, I built a function to 
specifically test whether the input date was in our data collection, if not, it will return a message to explain it was not. 

If the date entered was in our data, it will output a json response as instructed by task.

### Gunicorn
As the task is to tease out what my production level code would look like. I'm using gunicorn to run the flask application. This is containerised and initalised by my Dockerfile. 

### Application Factory
Also used the application factory format, which helps to build scalable, professional flask applications. I also used Blueprint to wrap around the function that handles all of the logic. 