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
| on the click site | click on website | it displays the websites info on the news |
|  |  |  |
|  |  |  |

## Known bugs

no bugs

## SetUp / Installation Requirements

### Prerequisites

* python3.6
* pip
* Virtual environment(virtualenv)

### Cloning

* In your terminal:

        ` $ git clone https://github.com/limobrian/News-Highlight.git

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
