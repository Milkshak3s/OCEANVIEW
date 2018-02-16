-- The mapping of temp ips to servers
CREATE TABLE `ip_server` (
	`server_name`	TEXT,
	`temp_ip`	TEXT,
	`creation_date`	TEXT,
	FOREIGN KEY(server_name) REFERENCES servers(server_name),
	FOREIGN KEY(temp_ip) REFERENCES temp_ips(temp_ip),
	PRIMARY KEY(`server_name`, `temp_ip`)
) WITHOUT ROWID;

-- These are the temp IPs that we know about
CREATE TABLE `temp_ips` (
	`temp_ip`   TEXT,
	`temp_int`  TEXT,
	`temp_dhcp` INT,
	PRIMARY KEY(`ip`)
) WITHOUT ROWID;

-- These are the servers that we know about
CREATE TABLE `servers` (
	`server_name`		TEXT,
	`server_ip`		TEXT,
	`server_description`	TEXT,
	`server_owner`		TEXT,
	PRIMARY KEY(`server_name`)
) WITHOUT ROWID;


-- Keep track of IP addresses that are not yet used
CREATE TABLE `available_ips` (
	`ip`		TEXT,
	PRIMARY KEY(`ip`)
) WITHOUT ROWID;

