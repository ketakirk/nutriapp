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

![Postman](https://cloud.githubusercontent.com/assets/11531183/9825843/ffb7200e-588a-11e5-9aae-4f97561ef124.jpg)

![Without response](https://cloud.githubusercontent.com/assets/11531183/9825847/071cded8-588b-11e5-9646-8dfdd14c1dd1.jpg)

![With response](https://cloud.githubusercontent.com/assets/11531183/9825854/0d9ff51a-588b-11e5-983d-dd7ed71898b1.jpg)

    


