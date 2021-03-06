# Pitcher
You can submit your one-minute or less pitch and other users will vote on it and leave comments to give their feedback on it. The pitches are organized by category.https://pitchrun.herokuapp.com/
## By Easther Mutheu

## Description
Pitcher is a web application that users can pitch ideas, comment and vote on other pitches. It requires for a new user to register and login to access some of the functions like add a pitch, comment and vote

## Specifications
* Users can view other people pitches
* Users can vote on other pitches
* Users can register and login to add new pitches and comment
* Users can submit pitches in four different categories

## Prerequisites
* Python 3.8 required

## Setup/Installation Requirements
Follow the following commands to run the project
* git clone/download ```git@github.com:easthermutheumwengei/pitcher.git```
* cd Pitch
* Edit the start.sh file with your api key from the pitcher.org website
* Install python 3.8
* Run ```chmod a+x start.py```
* Run ```./start.py```

### Behaviour Driven Development
| Behavior            | Input                         | Output                        |
| ------------------- | ----------------------------- | ----------------------------- |
| Index Page loads as default | Home link | Loads the home page. |
| View Categories | Home page or click on category | List of categories is displayed |
| View Business Pitch | Click on Business | Business Pitches are displayed|
| View Interview | Click on Interview | Interview Pitches are displayed|
| View Pick Up Lines | Click on Pick Up Lines | Pick Up Lines Pitches are displayed|
| View Technology | Click on Technology| Technology Pitches are displayed|
| Add new pitch | Click on New Pitch | Authentication page is displayed and users can add new pitches|
| Add Comment | Click on Comment | Form where user can fill in is displayed after login|



## Known Bugs
None known at the moment.

## Technologies Used
* Python
* HTML
* BOOTSTRAP
* Flask

## Support and contact details
In case of clarification email me at esthermutheu99@gmail.com

## License
*MIT*
Copyright (c) 2021 **Easther Mutheu**
