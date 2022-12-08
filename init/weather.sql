CREATE TABLE IF NOT EXISTS "weather" (
	"city" text,
	"country" text,
	"latitute" numeric(9,2),
	"longitude" numeric(9,2),
	"todays_date" date,
	"humidity" numeric(9,2),
	"pressure" numeric(9,2),
	"min_temp" numeric(9,2),
	"max_temp" numeric(9,2),
	"temp" numeric(9,2),
	"weather" text,
	PRIMARY KEY( city, todays_date )
);