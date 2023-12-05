Code Challenge Restaurants

This project simulates a system for managing restaurants, customers, and reviews similar to Yelp, providing functionalities for creating, accessing, and managing restaurant reviews.

Table of Contents

Introduction
Features
Installation
Usage
Project Structure
Contributing
License
Introduction

This Python project implements a basic system to manage restaurants, customers, and reviews using object-oriented programming principles. It consists of three main classes:

Customer: Represents a customer who can review restaurants.
Restaurant: Represents a restaurant that can be reviewed by customers.
Review: Represents a review made by a customer for a specific restaurant.
Features
Creation of customers, restaurants, and reviews.
Retrieval of customer details (full name, number of reviews) and restaurant details (average star rating, all reviews).
Association methods to link customers with restaurants and vice versa.
Aggregate methods to calculate average ratings and total reviews.
Class methods to find customers based on name parameters.
Installation
Clone the repository:

bash
Copy code
git clone <repository_url>
cd Code-Challenge-Restaurants
Install dependencies using pipenv:

bash
Copy code
pipenv install
Usage
Run the project:

bash
Copy code
pipenv run python -m lib.main
Test the code:

Execute the test cases by running the appropriate command.

Project Structure
lib/:

main.py: Entry point of the application.
customer.py: Contains the Customer class.
restaurant.py: Contains the Restaurant class.
review.py: Contains the Review class.
Pipfile, Pipfile.lock: Dependency management files.

Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or create a pull request.

License
This project is licensed under the MIT License.

feel free to look through this project.

happy coding!