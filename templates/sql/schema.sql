/******************************************************************************
  TODO:
  This is a place to define a script to create your database scheema. It should
  pretty much just a bunch of create statements
 *****************************************************************************/

CREATE TABLE messages(
  id INTEGER NOT NULL,
  message VARCHAR(500) NOT NULL,
  PRIMARY KEY(id)
);