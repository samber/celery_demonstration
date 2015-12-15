-- Table: credentials

-- DROP TABLE credentials;

CREATE TABLE credentials
(
  _id uuid NOT NULL,
  hostname character varying(255) NOT NULL,
  username character varying(255) NOT NULL,
  password character varying(255) NOT NULL,
  CONSTRAINT credentials_pkey PRIMARY KEY (_id)
)
WITH (
  OIDS=FALSE
);

ALTER TABLE credentials
  OWNER TO scanner;
