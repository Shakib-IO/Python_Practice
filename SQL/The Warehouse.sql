"1. Select all warehouses."
SELECT * FROM Warehouses;

"2. Select all boxes with a value larger than $150."
SELECT * FROM Boxes WHERE Value >150;

"3. Select all distinct contents in all the boxes."
SELECT DISTINCT Contents FROM Boxes ;

"4. Select the average value of all the boxes."
SELECT AVG(Value) FROM Boxes ; 

"5. Select the warehouse code and the average value of the boxes in each warehouse."
SELECT Warehouse, AVG(Value) FROM Boxes b GROUP BY Warehouse;

"6. Same as previous exercise, but select only those warehouses where the average value of the boxes is greater than 150."
SELECT Warehouse, AVG(Value) FROM Boxes GROUP BY Warehouse HAVING AVG(Value)>150;  

"7. Select the code of each box, along with the name of the city the box is located in."
SELECT b.Code, w.Location FROM Boxes b INNER JOIN Warehouses w ON b.Warehouse = w.Code;

"8. Select the warehouse codes, along with the number of boxes in each warehouse. Optionally, take into account that some warehouses are empty 
(i.e., the box count should show up as zero, instead of omitting the warehouse from the result)"
SELECT Warehouses.Code, COUNT(Boxes.Code) FROM Warehouses LEFT JOIN Boxes ON Warehouses.Code = Boxes.Warehouse GROUP BY Warehouses.Code;

"9. Select the codes of all warehouses that are saturated (a warehouse is saturated if the number of boxes in it is larger than the warehouse's capacity)."
SELECT warehouses.Code FROM Warehouses INNER JOIN Boxes ON Warehouses.Code  = Boxes.Warehouse GROUP BY Warehouses.Code, Warehouses.Capacity
HAVING COUNT(Boxes.Code)>Warehouses.Capacity ; 
"Alternative"
SELECT Code FROM Warehouses WHERE Capacity < (SELECT COUNT(*) FROM Boxes WHERE Warehouse = Warehouses.Code);

"10. Select the codes of all the boxes located in Chicago."
SELECT Code FROM Boxes WHERE Warehouse IN (SELECT Code FROM Warehouses WHERE Location = 'Chicago');

"11. Create a new warehouse in New York with a capacity for 3 boxes."
INSERT INTO Warehouses (Location,Capacity) VALUES ('New York',3);

"12. Create a new box, with code "H5RT", containing "Papers" with a value of $200, and located in warehouse 2."
INSERT INTO Boxes VALUES('H5RT','Papers',200,2);

"13. Reduce the value of all boxes by 15%."
 UPDATE Boxes SET Value = Value * 0.85;

"14. Apply a 20% value reduction to boxes with a value larger than the average value of all the boxes.
Attention: this solution doesn't work with MySQL 5.0.67: ERROR 1093 (HY000): You can't specify target table 'Boxes' for update in FROM clause"
 UPDATE Boxes SET Value = Value * 0.80 WHERE Value > (SELECT AVG(Value) FROM (SELECT * FROM Boxes) AS X);

"15. Remove all boxes with a value lower than $100."
DELETE FROM Boxes WHERE Value < 100;

"16. Remove all boxes from saturated warehouses."
DELETE FROM Boxes WHERE Warehouse IN ( SELECT Code FROM Warehouses WHERE Capacity < ( SELECT COUNT(*) FROM Boxes WHERE Warehouse = Warehouses.Code ) );