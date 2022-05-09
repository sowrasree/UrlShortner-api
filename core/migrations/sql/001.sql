create table users (
	id varchar(255) primary key,
	email varchar(255) not null unique,
	encrypted_password varchar(255),
	full_name varchar(255) not null,
	mobile varchar(255)
);