CREATE TABLE `Training_Program` (
    `Program_ID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `Program_Name` TEXT NOT NULL,
    `Program_Description` TEXT NOT NULL
);

CREATE TABLE `Training_Program_Sessions` (
    `Session_ID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `Program_ID` INTEGER NOT NULL,
    `Program_Start_Date` TEXT NOT NULL,
    `Program_End_Date` TEXT NOT NULL,
    `Max_Students` INTEGER NOT NULL,
    FOREIGN KEY (Program_ID) REFERENCES Training_Program (Program_ID)
);

CREATE TABLE `Person` (
	`Person_ID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`First_Name`	TEXT NOT NULL,
	`Last_Name`	TEXT NOT NULL,
	`Street`	TEXT,
	`City`	TEXT,
	`State`	TEXT,
	`Zip`	NUMERIC,
	`Phone`	TEXT,
	`Email`	TEXT
);

CREATE TABLE `Employee` (
	`Employee_ID`	TEXT NOT NULL UNIQUE,
	`Person_ID`	INTEGER NOT NULL UNIQUE,
	`Dept_ID`	INTEGER NOT NULL,
	`Comp_ID`	INTEGER NOT NULL,
	`Employee_Is_Active`	INTEGER NOT NULL,
	PRIMARY KEY(`Employee_ID`),
    FOREIGN KEY (Person_ID) REFERENCES Person (Person_ID),
    FOREIGN KEY (Dept_ID) REFERENCES Department (Department_ID),
    FOREIGN KEY (Comp_ID) REFERENCES Computer (Comp_ID)
);

CREATE TABLE `Employment_Dates` (
    `Employee_ID` TEXT NOT NULL,
    `Hire_Date` TEXT NOT NULL,
    `Term_Date` TEXT,
    FOREIGN KEY (Employee_ID) REFERENCES Employee (Employee_ID)
);

CREATE TABLE `Department` (
    `Department_ID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `Dept_Name` TEXT NOT NULL,
    `Supervisor` INTEGER,
    `Remaining_Budget` INTEGER
);

CREATE TABLE `Computer` (
    `Comp_ID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `Commission_Date` TEXT NOT NULL,
    `Decommission_Date` TEXT
);

CREATE TABLE `Employee_Training` (
    `Session_ID` INTEGER NOT NULL,
    `Employee_ID` TEXT NOT NULL,
    `Completed` INTEGER NOT NULL,
    FOREIGN KEY (Session_ID) REFERENCES Training_Program (Session_ID),
    FOREIGN KEY (Employee_ID) REFERENCES Employee (Employee_ID)
);

CREATE TABLE `Product` (
    `Product_ID` INTEGER NOT NULL AUTOINCREMENT PRIMARY KEY UNIQUE,
    `Type_ID` INTEGER NOT NULL,
    `Seller_ID` INTEGER NOT NULL,
    `Title` TEXT NOT NULL,
    `Price` INTEGER NOT NULL,
    `Description` TEXT,
    FOREIGN KEY (Type_ID) REFERENCES Product_Types (Type_ID),
    FOREIGN KEY (Seller_ID) REFERENCES Seller (Seller_ID)
);

CREATE TABLE `Product_Type` (
    `Type_ID` INTEGER NOT NULL AUTOINCREMENT PRIMARY KEY UNIQUE,
    `Type_Name` Text NOT NULL
);

CREATE TABLE `Seller` (
    `Seller_ID` TEXT NOT NULL PRIMARY KEY UNIQUE,
    `Person_ID` INTEGER NOT NULL UNIQUE,
    `Seller_Is_Active` INTEGER NOT NULL,
    FOREIGN KEY (Person_ID) REFERENCES Person(Person_ID)
);

CREATE TABLE `Customer` (
    `Customer_ID` TEXT NOT NULL PRIMARY KEY UNIQUE,
    `Person_ID` INTEGER NOT NULL UNIQUE,
    `Customer_Create_Date` TEXT NOT NULL,
    `Last_Signon` TEXT NOT NULL,
    FOREIGN KEY (Person_ID) REFERENCES Person(Person_ID)
);

CREATE TABLE `Order` (
    `Order_ID` INTEGER AUTOINCREMENT PRIMARY KEY UNIQUE NOT NULL,
    `Customer_ID` TEXT NOT NULL,
    `Payment_ID` INTEGER,
    `Is_Complete` INTEGER NOT NULL,
    `Is_Shipped` INTEGER NOT NULL,
    `Order_Date` TEXT NOT NULL,
    `Total_Amount` INTEGER NOT NULL,
    FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID),
    FOREIGN KEY (Payment_ID) REFERENCES Payment_Options(Payment_ID)
);

CREATE TABLE `Ordered_Products` (
    `Order_ID` INTEGER NOT NULL,
    `Product_ID` INTEGER NOT NULL,
    FOREIGN KEY (Order_ID) REFERENCES Order(Order_ID),
    FOREIGN KEY (Product_ID) REFERENCES Product(Product_ID)
);

CREATE TABLE `Payment_Options` (
    `Payment_ID` PRIMARY KEY INTEGER NOT NULL UNIQUE AUTOINCREMENT,
    `Customer_ID` TEXT NOT NULL,
    `Account_Num` TEXT NOT NULL,
    `Payment_Type
)