# Project 2: Tailored

## Project Description

Tailored is a client to photographer site built to match clients to their perfect photographer based on location, price point, and expertise. Based on these criteria, users will be able to search the registered database based on their needs. Users will also be able to "search all" to view all available photographers beyond any set criteria. This will be developed using Python and Django.  

## Project Links
- yet to deploy 

## Wireframes
[Wireframe](https://xd.adobe.com/view/dc59ec26-1690-401f-5bf2-36ad1635f269-aa68/)

<!-- ## Designs: -->


<!-- - client request to design -->

## MVP/ Post-MVP

### MVP:
- landing homepage -- pic carausel, login/signup links, "browse all" button/ link
- Photographer login -- authentication  
- browse all photographers
- Photographer home/ profile -- Individual photographer apps/ pages. This will also have a separate booking page

### Post-MVP:
- User/Client side
- Extensive searchabilty using ElasticSearch

- User/client login -- authentication 
- User/client signup
- User/client home page
- Searchabilty using ElasticSearch 

## Structure:

### Templates:

| Template  |                          Description                          |
| --------------- | :-----------------------------------------------------------: |
| Landing       |           Landing page where user can click to browse/ search all photographers, click to advanced search, click to login, click to sign up  |
<!-- | Login         |           User can log in to user account          |
| Sign Up       |           User sign up for user account            | -->
| Browse All        |       GATEWAYED -- only allows authenticated users to enter. All photographer's listed accounts linking to their homepage without any search criteria         |
<!-- | Advanced Search   |       GATEWAYED -- only allows authenticated users to enter. User can search for photographers based on zip, price, specialty -- user authentication         | -->
<!-- | User Home         |       User's saved/ favorited photographers, account details              | -->
| Photographer Home |       Photographer's homepage/ sitepage        |
| Book photographer |       Clients can contact photographer and book with photographer through page.       |

## Architecture:
APP 1: Tailored
models: Photographer, Shoots

## Time Frames

| Component                       | Priority | Estimated Time | Time Invested | Actual Time |
| ------------------------------- | :------: | :------------:  | :-----------:  | :---------: |
| Planning & Wireframing          |    H     |      3hrs       |      hrs       |     hrs     |
| Build file structure            |    H     |      2hrs       |      hrs       |     hrs     |
| Views                           |    H     |      4hrs       |      hrs       |     hrs     |
| Templates                       |    H     |      2hrs       |      hrs       |     hrs     |
| Client Login                    |    H     |      3hrs       |      hrs       |     hrs     |
| Photographer Login              |    H     |      3hrs       |      hrs       |     hrs     |
| ElasticSearch                   |    H     |      7hrs       |      hrs       |     hrs     |
| Styling                         |    H     |      8hrs       |      hrs       |     hrs     |
| Documentation                   |    H     |      3hrs       |      hrs       |     hrs     |
| Total                           |    H     |       hrs       |      hrs       |     hrs     |

## Technologies Used
- Python
- Django 

## Additional Libraries
- Bootstrap / Django Crispy Forms
- ElasticSearch 