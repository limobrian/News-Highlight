# News Highlights

## By **limooh brian**

## Description

This is a news application that allows a user to view news from different networks in different parts of the world. It has a list of all the news sources from which the user can pick and read the news directly from the source's site. A user can also search for whatever news using a key word.

## Technologies used

python

## Behaviour Driven Development(BDD)

| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| on the site | click on the view airtcles |  displays all the articles news |

## Known bugs

no bugs

## SetUp / Installation Requirements

### Prerequisites

* python3.6
* pip
* Virtual environment(virtualenv)

### Cloning

* In your terminal:

       ` $ git clone 
       ` $ cd new-highlight

### Creating the virtual environment

`$ python3.6 -m venv --without-pip virtual

`$ source virtual/bin/env

`$ curl https://bootstrap.pypa.io/get-pip.py | python

### Installing Flask and other Modules

        `$ python3.6 -m pip install Flask

        `$ python3.6 -m pip install Flask-Bootstrap

        `$ python3.6 -m pip install Flask-Script

## Setting up the API Key

To be able to gather article info from the News API you will need an API Key.
Visit https://newsapi.org/ and register for an API key.
In the root directory of the project folder create a file: start.sh
Insert the following info into it:
export NEWS_API_KEY=''
python3.6 manage.py server
Insert the API Key you received from News Api where is.

## Running the Application

* To run the application, in your terminal:

        `$ chmod a+x start.sh
        `$ ./start.sh

## LICENSE

The application is under an [MIT License].

## Contact Information

You can contact me via my gmail account limobrian290@gmail.com



Setup/Installation Requirements
Prerequisites
python3.6
pip
Virtual environment(virtualenv)
Cloning and running
Clone the application using git clone(this copies the app onto your device). In terminal:
$ git clone https://github.com/DMGithinji/News-reel
$ cd news_app
Creating the virtual environment
$ python3.6 -m venv --without-pip virtual
$ source virtual/bin/env
$ curl https://bootstrap.pypa.io/get-pip.py | python
Installing Flask and other Modules
$ python3.6 -m pip install Flask
$ python3.6 -m pip install Flask-Bootstrap
$ python3.6 -m pip install Flask-Script
Setting up the API Key
To be able to gather article info from the News API you will need an API Key.
Visit https://newsapi.org/ and register for an API key.
In the root directory of the project folder create a file: start.sh
Insert the following info into it:
export NEWS_API_KEY=''
python3.6 manage.py server
Insert the API Key you received from News Api where is.
Run the application:
$ chmod a+x start.sh
$ ./start.sh
Testing the Application
To run the tests for the class files:
$ python3.6 manage.py test
Technologies Used
Python 3.6
Flask
Behaviour driven development/ Specifications
Behaviour    Input    Output
On the site    Click a source    Redirects to source page with articles from the source
Read article on site    Click on 'Read more..'    Takes you to article on source site
On the sete    Click on category    Takes you to page with sources covering that category
Live site
You can view the live site here
