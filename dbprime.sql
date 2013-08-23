DROP DATABASE IF EXISTS "foodportal";

CREATE DATABASE "foodportal" ENCODING 'UTF8';
ALTER DATABASE "foodportal" OWNER TO foodportal;

\connect foodportal foodportal

BEGIN;
create table "public"."users"(
"name" TEXT NOT NULL,
"uid" TEXT PRIMARY KEY,
"venmo_username" TEXT NOT NULL,
"balance" MONEY
)
WITHOUT OIDS;

create table "public"."transactions"(
"uid" TEXT NOT NULL,
"items" TEXT[],
"timestamp" TEXT PRIMARY KEY,
"amount" MONEY NOT NULL,
"type" TEXT NOT NULL
)
WITHOUT OIDS;

create table "public"."items"(
"name" TEXT NOT NULL,
"uid" TEXT PRIMARY KEY,
"cost" MONEY NOT NULL,
"section" TEXT NOT NULL,
"is_current" BOOL NOT NULL,
"event" TEXT NOT NULL
)
WITHOUT OIDS;

create table "public"."events"(
"name" TEXT NOT NULL,
"uid" TEXT PRIMARY KEY,
"date" DATE NOT NULL,
"dueTime" TIME NOT NULL,
"foodEta" TIME NOT NULL,
"organizer_uid" TEXT NOT NULL,
"description" TEXT
)
WITHOUT OIDS;
COMMIT;

BEGIN;
COMMENT ON TABLE "users" is 'table containing all the users, and some information about them';
COMMENT ON COLUMN "users"."name" is 'Name of the user';
COMMENT ON COLUMN "users"."uid" is 'uid of the user';
COMMENT ON COLUMN "users"."venmo_username" is 'Venmo username of the user';
COMMENT ON COLUMN "users"."balance" is 'balance of the user';
COMMIT;

BEGIN;
COMMENT ON TABLE "transactions" is 'table containing all the transactions, and some information about them';
COMMENT ON COLUMN "transactions"."uid" is 'uid of the user making the transaction';
COMMENT ON COLUMN "transactions"."items" is 'An array of the items purchased in the transaction';
COMMENT ON COLUMN "transactions"."amount" is 'Total amount of money transferred by this transaction';
COMMENT ON COLUMN "transactions"."type" is 'purchase or deposit';
COMMIT;

BEGIN;
COMMENT ON TABLE "items" is 'table containing all the items available for purchase, and some information about them';
COMMENT ON COLUMN "items"."uid" is 'uid of the item';
COMMENT ON COLUMN "items"."cost" is 'The cost of this item';
COMMENT ON COLUMN "items"."section" is 'The section of the menu this item belongs to';
COMMENT ON COLUMN "items"."is_current" is 'whether or not this item is currently for sale';
COMMENT ON COLUMN "items"."event" is 'the name of the event this item belongs to';
COMMIT;

BEGIN;
COMMENT ON TABLE "events" is 'table containing all the events that have taken place, in addition to upcoming ones, and some information about them';
COMMENT ON COLUMN "events"."name" is 'name of the event';
COMMENT ON COLUMN "events"."uid" is 'uid of the event';
COMMENT ON COLUMN "events"."date" is 'date of the event';
COMMENT ON COLUMN "events"."dueTime" is 'The time the orders are due';
COMMENT ON COLUMN "events"."foodEta" is 'The estimated arrival time of the food';
COMMENT ON COLUMN "events"."organizer_uid" is 'The uid of the events organizer';
COMMENT ON COLUMN "events"."description" is 'The description of the event';
COMMIT;
