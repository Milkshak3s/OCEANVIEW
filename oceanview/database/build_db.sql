-- The database layout for OCEANVIEW
-- Micah Martin

-- Keep track of arbitrary information sent up by the host
CREATE TABLE `data` (
  `id`        INTEGER,
	`ip`    TEXT,
	`name`  TEXT,
	`data`	TEXT,
  `time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
	      PRIMARY KEY(`id` ASC)
) ;

-- These are the IPs that we know about with last checkin time
CREATE TABLE `timestamps` (
  `id`        INTEGER,
	`ip`   TEXT,
	`time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
	      PRIMARY KEY(`id` ASC)
) ;


-- Keystroke data that we have captured
CREATE TABLE `keystrokes` (
  `id`        INTEGER,
	`ip`        TEXT,
  `keystroke` TEXT,
	`time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
	      PRIMARY KEY(`id` ASC)
) ;

-- Store screenshots sent up from the client
CREATE TABLE `files` (
  `id`        INTEGER,
	`ip`        TEXT,
  `filename`  TEXT,
	`time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
	      PRIMARY KEY(`id` ASC)
) ;

-- Store tags for hosts set by the user
CREATE TABLE `tags` (
  `id`        INTEGER,
	`ip`        TEXT,
  `tag`				TEXT,
        PRIMARY KEY(`id` ASC)
);

-- Assign a unique identifier to hosts based on their MAC and LAN addresses
CREATE TABLE `identities` (
  `id`  INTEGER,
  `ip`  TEXT,
  `mac` TEXT,
        PRIMARY KEY(`id` ASC)
);
