-- Creates schema for profiles table

drop table if exists profiles;

create table profiles (
	food_id varchar(100),
	food_code varchar(100),
	display_name varchar(100),
	portion_default varchar(100),
	portion_amt varchar(100),
	solid_fats varchar(100),
	added_sugars varchar(100),
	calories varchar(100),
	saturated_fats varchar(100)
);

copy profiles--
from '/Users/rohan/Documents/code/python/nutriapp/data/beautiful_soup_xml_final/food.csv'--
with delimiter ':';

