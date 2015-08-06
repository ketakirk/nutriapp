-- Creates schema for profiles table

drop table if exists profiles;

create table profiles (
	profile_id varchar(36),
	first_name varchar(50),
	last_name varchar(50),
	state varchar(50)
);

copy profiles--
from '/Users/rohan/Documents/code/python/webapp0/data/profiles.csv'--
with delimiter ',';

