### About

Nutriapp provides nutritional information for common food items. This is an end-to-end application written in Python built using the Flask framework.

### Libraries used:
* BeautifulSoup
* psycopg2
* uuid
* json

### App overview
The nutrition data was extracted from the [Government food database](http://catalog.data.gov/dataset/mypyramid-food-raw-data-f9ed6) and was cleaned using the BeautifulSoup library. The cleaned data is fed to a backend Postgres database, and made available through CRUD operations written in Python. Finally, the data is presented through a simple Javascript front end.

This is a work in progress. Currently, the food items are searchable by unique identifiers. The goal is to create an application where the food items can be searched using interesting attributes such as calorie content or processed sugar contents. 

### Sample response:
Here are the screenshots of responses from Postman and the browser.

![Postman](https://github.com/ketakirk/nutriapp/app/static/images/postman.jpg)

    


