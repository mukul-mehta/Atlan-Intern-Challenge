# Atlan-Collect Challenge

This repository contains code written as part of the challenge for a winter internship at Atlan. 


### Tools Used

* Python 
* Flask with Blueprints
* SQLAlchemy with Postgre SQL
* HTML
* Docker
* Gunicorn to deploy on Heroku
* Pipenv for package management 

### Installation and Setup Instructions

* Clone this repository by running `git clone https://github.com/mukul-mehta/Atlan-Intern-Challenge.git`
* Generate the random test data by running `python randomDataGen.py` present in the `app` directory. This will generate CSV Files for all 3 relevant cases in the `app/test-data` directory. 

I've used Docker to containerize the app for easy deployment. To run the app with Docker:

* Install docker and docker-compose
* `cd /path/to/project/`
* `docker-compose up`  # this will build only the first time, to rebuild add `--build`
* Access the endpoints on 127.0.0.1:5000

#### To Run without Docker
* Make sure you have `Python` and `pip` installed. 
* Run `pip install pipenv`
* `cd /path/to/project`
* `pipenv install`
* `pipenv shell`
* `python manage.py` and then access the endpoints on localhost:5000

### Documentation

The endpoints have been documented using python-docstrings and some information has also been presented on the HTML pages for each example.

### TO-DO's

Due to my academic engagements, I tried to work on as many features as I could add to the application. It was very fun working on the task and I learnt multiple new things. It took me quite some effort to understand the PS and there were implementation roadblocks to be conquered. 

I feel the following things could be done to make the app better

#### Create a GUI and add a Progress Bar

Instead of sending a request to /exNo/stopUpload, we could make a frontend using JSJS which shows a progress bar. On pressing a stop button, the process terminates rather than having to send a request to do so. 

#### Heroku Deployment isn't working
I tried deploying the app on heroku using the Docker image but couldn't complete the deployment process. The process shouldn't take too much time though since the docker container is working as expected. 

#### Deploy on a Kubernetes cluster

I started reading up about Kubernetes and did the tutorial on their website but I couldn't create a cluster and deploy this application to the cluster. 

### Improve process of importing from CSV File to SQL Table
I started out by importing the CSV as a pandas dataframe and using the inbuilt to_sql method to convert it to a MySQL table. This method was ineffecient and took too much time and CPU to complete the process. I then switched to using the COPY_FROM method using PostgreSQL+ psycopg2. This was a significant speed improvement but the process can be further improved by adding multithreading and using optimized SQL operations. 

