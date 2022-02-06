"Create All the Tables"

 CREATE TABLE Employee (
   EmployeeID INTEGER PRIMARY KEY NOT NULL,
   Name TEXT NOT NULL,
   Position TEXT NOT NULL,
   Salary REAL NOT NULL,
   Remarks TEXT
 );
 
 CREATE TABLE Planet (
   PlanetID INTEGER PRIMARY KEY NOT NULL,
   Name TEXT NOT NULL,
   Coordinates REAL NOT NULL
 );
 
 CREATE TABLE Shipment (
   ShipmentID INTEGER PRIMARY KEY NOT NULL,
   Date TEXT,
   Manager INTEGER NOT NULL
     CONSTRAINT fk_Employee_EmployeeID REFERENCES Employee(EmployeeID),
   Planet INTEGER NOT NULL
     CONSTRAINT fk_Planet_PlanetID REFERENCES Planet(PlanetID)
 );
 
 CREATE TABLE Has_Clearance (
   Employee INTEGER NOT NULL
     CONSTRAINT fk_Employee_EmployeeID REFERENCES Employee(EmployeeID),
   Planet INTEGER NOT NULL
     CONSTRAINT fk_Planet_PlanetID REFERENCES Planet(PlanetID),
   Level INTEGER NOT NULL,
   PRIMARY KEY(Employee, Planet)
 );
 
 CREATE TABLE Client (
   AccountNumber INTEGER PRIMARY KEY NOT NULL,
   Name TEXT NOT NULL
 );
 
 CREATE TABLE Package (
   Shipment INTEGER NOT NULL
     CONSTRAINT fk_Shipment_ShipmentID REFERENCES Shipment(ShipmentID),
   PackageNumber INTEGER NOT NULL,
   Contents TEXT NOT NULL,
   Weight REAL NOT NULL,
   Sender INTEGER NOT NULL
     CONSTRAINT fk_Client_AccountNumber REFERENCES Client(AccountNumber),
   Recipient INTEGER NOT NULL
     CONSTRAINT fk_Client_AccountNumber REFERENCES Client(AccountNumber),
   PRIMARY KEY(Shipment, PackageNumber)
 );
 
"Add all Data"
INSERT INTO Client VALUES(1, 'Zapp Brannigan');
INSERT INTO Client VALUES(2, "Al Gore's Head");
INSERT INTO Client VALUES(3, 'Barbados Slim');
INSERT INTO Client VALUES(4, 'Ogden Wernstrom');
INSERT INTO Client VALUES(5, 'Leo Wong');
INSERT INTO Client VALUES(6, 'Lrrr');
INSERT INTO Client VALUES(7, 'John Zoidberg');
INSERT INTO Client VALUES(8, 'John Zoidfarb');
INSERT INTO Client VALUES(9, 'Morbo');
INSERT INTO Client VALUES(10, 'Judge John Whitey');
INSERT INTO Client VALUES(11, 'Calculon');

INSERT INTO Employee VALUES(1, 'Phillip J. Fry', 'Delivery boy', 7500.0, 'Not to be confused with the Philip J. Fry from Hovering Squid World 97a');
INSERT INTO Employee VALUES(2, 'Turanga Leela', 'Captain', 10000.0, NULL);
INSERT INTO Employee VALUES(3, 'Bender Bending Rodriguez', 'Robot', 7500.0, NULL);
INSERT INTO Employee VALUES(4, 'Hubert J. Farnsworth', 'CEO', 20000.0, NULL);
INSERT INTO Employee VALUES(5, 'John A. Zoidberg', 'Physician', 25.0, NULL);
INSERT INTO Employee VALUES(6, 'Amy Wong', 'Intern', 5000.0, NULL);
INSERT INTO Employee VALUES(7, 'Hermes Conrad', 'Bureaucrat', 10000.0, NULL);
INSERT INTO Employee VALUES(8, 'Scruffy Scruffington', 'Janitor', 5000.0, NULL);

INSERT INTO Planet VALUES(1, 'Omicron Persei 8', 89475345.3545);
INSERT INTO Planet VALUES(2, 'Decapod X', 65498463216.3466);
INSERT INTO Planet VALUES(3, 'Mars', 32435021.65468);
INSERT INTO Planet VALUES(4, 'Omega III', 98432121.5464);
INSERT INTO Planet VALUES(5, 'Tarantulon VI', 849842198.354654);
INSERT INTO Planet VALUES(6, 'Cannibalon', 654321987.21654);
INSERT INTO Planet VALUES(7, 'DogDoo VII', 65498721354.688);
INSERT INTO Planet VALUES(8, 'Nintenduu 64', 6543219894.1654);
INSERT INTO Planet VALUES(9, 'Amazonia', 65432135979.6547);

INSERT INTO Has_Clearance VALUES(1, 1, 2);
INSERT INTO Has_Clearance VALUES(1, 2, 3);
INSERT INTO Has_Clearance VALUES(2, 3, 2);
INSERT INTO Has_Clearance VALUES(2, 4, 4);
INSERT INTO Has_Clearance VALUES(3, 5, 2);
INSERT INTO Has_Clearance VALUES(3, 6, 4);
INSERT INTO Has_Clearance VALUES(4, 7, 1);

INSERT INTO Shipment VALUES(1, '3004/05/11', 1, 1);
INSERT INTO Shipment VALUES(2, '3004/05/11', 1, 2);
INSERT INTO Shipment VALUES(3, NULL, 2, 3);
INSERT INTO Shipment VALUES(4, NULL, 2, 4);
INSERT INTO Shipment VALUES(5, NULL, 7, 5);

INSERT INTO Package VALUES(1, 1, 'Undeclared', 1.5, 1, 2);
INSERT INTO Package VALUES(2, 1, 'Undeclared', 10.0, 2, 3);
INSERT INTO Package VALUES(2, 2, 'A bucket of krill', 2.0, 8, 7);
INSERT INTO Package VALUES(3, 1, 'Undeclared', 15.0, 3, 4);
INSERT INTO Package VALUES(3, 2, 'Undeclared', 3.0, 5, 1);
INSERT INTO Package VALUES(3, 3, 'Undeclared', 7.0, 2, 3);
INSERT INTO Package VALUES(4, 1, 'Undeclared', 5.0, 4, 5);
INSERT INTO Package VALUES(4, 2, 'Undeclared', 27.0, 1, 2);
INSERT INTO Package VALUES(5, 1, 'Undeclared', 100.0, 5, 1);

"1. Who received a 1.5kg package?"
SELECT Client.Name FROM Client JOIN Package ON Client.AccountNumber = Package.Recipient WHERE Package.weight = 1.5; 

"2. What is the total weight of all the packages that he sent?"
SELECT SUM(p.weight) FROM Client AS c JOIN Package AS p ON c.AccountNumber = p.Sender WHERE c.Name = "Al Gore's Head";

"Which pilots transported those packages?"
SELECT Employee.Name
FROM Employee
  JOIN Shipment ON Shipment.Manager = Employee.EmployeeID
  JOIN Package ON Package.Shipment = Shipment.ShipmentID
WHERE Shipment.ShipmentID IN (
  SELECT p.Shipment 
  FROM Client AS c 
    JOIN Package as P 
    ON c.AccountNumber = p.Sender
  WHERE c.AccountNumber = (
    SELECT Client.AccountNumber
    FROM Client JOIN Package 
      ON Client.AccountNumber = Package.Recipient 
    WHERE Package.weight = 1.5
  )
)
GROUP BY (Employee.Name);


