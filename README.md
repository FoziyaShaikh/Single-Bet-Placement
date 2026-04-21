# Single-Bet-Automation
Single Bet Placement is a sports betting web application that allows users to place a single wager on the outcome of a sporting event. 
This repository contains a Python-based automation framework for testing both web UI and API modules.

# Set Up Instructions
1. Clone the repository
   git clone https://github.com/your-username/QA-AUTOMATION-PROJECT.git
2. Navigate to the repossitory
   cd QA-AUTOMATION-PROJECT
   
# Project Structure
1. api/ - All API tests
2. config/ -Settings file contains all global settings and variables and __init__ file allow to import as a package.      
4. pages/ -All page object locators and functions
5. tests/ -All UI test files
6. confest/ -All pytest fixtures
   
# Install Dependencies
1. install python 3
2. Install libraries using pip command:- pytest, requests and selenium

# Running tests
1. pytest - to run all tests
2. pytest tests/test_single_bet.py - to run single test
3. pytest -s api/test_place_bet_api_validation.py - to see the print statement for results
