CREATE TABLE LOCATION (
	loc_id varchar NOT NULL,
	loc_type varchar,
	loc_name varchar,
	longitude FLOAT,
	latitude FLOAT,
	start_date DATE,
	end_date DATE,
	country varchar NOT NULL,
	time_zone varchar,
	info varchar,
	CONSTRAINT LOCATION_pk PRIMARY KEY (loc_id)
) WITH (
  OIDS=FALSE
);



CREATE TABLE TRAIN (
	train_id varchar NOT NULL,
	company_1_id varchar NOT NULL,
    company_2_id varchar,
	ser_character varchar,
	pricing_cat integer,
	item_des integer,
	start_date DATE,
	end_date DATE,
	period_days varchar NOT NULL,
	train_type varchar,
    start_loc varchar NOT NULL,
    end_loc varchar NOT NULL,
	CONSTRAINT TRAIN_pk PRIMARY KEY (train_id,company_1_id,period_days,start_date,end_date,start_loc,end_loc)
) WITH (
  OIDS=FALSE
);



CREATE TABLE TIMETABLE (
	train_id BINARY NOT NULL,
	loc_id BINARY NOT NULL,
	arrival_time TIME,
	departure_time TIME,
	itinerary integer NOT NULL,
	id serial NOT NULL,
	CONSTRAINT TIMETABLE_pk PRIMARY KEY (id)
) WITH (
  OIDS=FALSE
);





ALTER TABLE TIMETABLE ADD CONSTRAINT TIMETABLE_fk0 FOREIGN KEY (train_id) REFERENCES TRAIN(train_id);
ALTER TABLE TIMETABLE ADD CONSTRAINT TIMETABLE_fk1 FOREIGN KEY (loc_id) REFERENCES LOCATION(loc_id);
