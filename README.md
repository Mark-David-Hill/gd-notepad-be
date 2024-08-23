# gd-notepad-be

Overview

This is the backend for a Game Design Notepad app, which is designed to make it easier to analyze the different parts of a game and take notes on them. I made this for my Dev Pipeline Backend Course Capstone project.

I learned a lot this semester, but one of the most significant things I feel I learned was getting to know the workflow of the backend well enough that I could troubleshoot and find the source of problems when things weren't working. This was very difficult for me at the beginning of the semester, so it was satisfying to be able to begin to understand better how things were related so I could solve problems as they arose.

My favorite part of this Backend course was seeing everything come together over the course of the semester. We started small, but it was satisfying to add each successive piece until I was able to build out an entire backend myself (with help from my instructors). Finishing this capstone was challenging but also interesting and a lot of fun.

Getting Started

## run the following commands to start the backend

python3 -m pipenv shell
pipenv install
createdb gd-notepad
python app.py

There is a Postman Collection included which allows you to test the requests. You can start by creating a user and then authenticating them. This give you access to other requests. Refer to the included ERD to see what tables require other tables.

The included tables are:
-App Users
-Auth Tokens
-Game Elements
-Games
-Release Profiles
-Types
-Tags
-Notes
-Element Relationships
-Game Elements Tags Xref

I plan on adding additional requests and eventually making a frontend for this app, but it should be functional as a backend in its current state.
