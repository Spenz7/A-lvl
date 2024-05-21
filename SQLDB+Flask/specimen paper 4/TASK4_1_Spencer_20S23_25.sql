CREATE TABLE `Device` (
	`SerialNumber`	INTEGER ,
	`Type`	TEXT,
	`Model`	TEXT,
	`Location`	TEXT,
	`DateOfPurchase`	INTEGER,
	`WrittenOff`	INTEGER,
	PRIMARY KEY(`SerialNumber`)
);

CREATE TABLE `Laptop` (
	`SerialNumber`	INTEGER,
	`WeightKg`	REAL,
	FOREIGN KEY(`SerialNumber`) REFERENCES `Device`(`SerialNumber`),
	PRIMARY KEY(`SerialNumber`)
);

CREATE TABLE `Monitor` (
	`SerialNumber`	INTEGER,
	`DateCleaned`	TEXT,
	FOREIGN KEY(`SerialNumber`) REFERENCES `Device`(`SerialNumber`),
	PRIMARY KEY(`SerialNumber`)
);

CREATE TABLE `Printer` (
	`SerialNumber`	INTEGER,
	`Toner`	TEXT,
	`DateChanged`	TEXT,
	FOREIGN KEY(`SerialNumber`) REFERENCES `Device`(`SerialNumber`),
	PRIMARY KEY(`SerialNumber`)
);