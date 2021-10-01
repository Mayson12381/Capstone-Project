<!-- ABOUT THE PROJECT -->
## About The Project

This project was created for the Capstone Project in conjunction with the Bachelor Thesis of Patrick Weber for the Bachelor of Science in Software Engineering at CODE University of Applied Sciences.

The goal of this project is to provide the user with an interface to interact with the result of the Bachelor Thesis, which is a Machine Learning Algorithm to support Esports Teams with strategy success predictions to step up their game and focus more on playing instead of calculating odds.

The product is seperated into three parts.

1. A Python script running on the computer of the player, that is capturing live gameplay to read game information and provide that data to a database for further processing.
2. A Vue.js web application that displays captured data from the python client and allows further tweaking of input parameters of the ML algorithm and an overview of past results.
3. A firebase backend that handles user authentication, api requests and the database

This split was mainly done, so the players can focus on playing and the interaction with the ML algorithm can be done by someone other than the players.

<!-- GETTING STARTED -->
## Getting Started

To set up both programs, please follow the instructions in each readme file in *capstone-project-vue* and *capstone-project-python* respectively.

The webpage is also live at -> https://capstone-project-pweber.web.app/

## Demo

To see a demo of the application, please visit the following link:

* https://youtu.be/FQ8RAJkoHYQ

## Contribution

Since this is a Monorepo, we have some guidelines to achieve better structure and overview:

### Branches

Are always prefixed with either *comp* or *web* and usually have one of the following names:

- feature/ - feature branch
- test/ - test branch
- fix/ fix branch

### Commit Messages

Follow the following pattern:

[*package_name*] - *type*: *summary*]

- package_name: Web (frontend), Comp (client-side preprocessor)
- type: feat, fix, test, docs, refactor
- summary in the present tense

And messages are prefixed with git commit emojies from this list -> https://gist.github.com/parmentf/035de27d6ed1dce0b36a

## Requirements and Validation

My requirement list and Interview validation can be found in *requirements_and_validation.md*