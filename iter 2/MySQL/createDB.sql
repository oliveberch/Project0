create database inflation_records;
use inflation_records;

-- Table 1: CountryInfo
CREATE TABLE CountryInfo (
    CountryCode VARCHAR(3) PRIMARY KEY,
    Country VARCHAR(255),
    Region VARCHAR(255)
);

-- Table 2: GDPDeflatorData
CREATE TABLE InflationData (
    CountryCode VARCHAR(3),
    Year INT,
    Inflation FLOAT,
    primary key (CountryCode, YEAR)
    FOREIGN KEY (CountryCode) REFERENCES CountryInfo(CountryCode)
);
    
-- Table 3: Users
CREATE TABLE Users (
    UserID INT PRIMARY KEY,
    PASS VARCHAR(255)
);