"9. Select the name and price of all products with a price larger than or equal to $180, 
and sort first by price (in descending order), and then by name (in ascending order)."
SELECT Name, Price FROM Products WHERE Price >= 180 ORDER BY Price DESC, Name;

"10. Select all the data from the products, including all the data for each products manufacturer."
SELECT * FROM Products, Manufacturers WHERE Products.Manufacturer = Manufacturers.Code;

"11. Select the product name, price, and manufacturer name of all the products."
SELECT Products.Name, Products.Price, Manufacturers.Name from Products INNER JOIN Manufacturers
ON Products.Manufacturer = Manufacturers.Code 

"12. Select the average price of each manufacturer's products, showing only the manufacturer's code."
SELECT AVG(Price), Manufacturer from Products GROUP BY Manufacturer;

"13. Select the average price of each manufacturer's products, showing the manufacturer's name."
SELECT Manufacturers.Name, AVG(Price) FROM Products INNER JOIN Manufacturers 
ON products.Manufacturer = Manufacturers.Code GROUP BY Manufacturers.Name;

"14. Select the names of manufacturer whose products have an average price larger than or equal to $150."
SELECT Manufacturers.Name, AVG(Price) from Products INNER JOIN Manufacturers 
ON products.Manufacturer = Manufacturers.Code GROUP BY Manufacturers.Name HAVING AVG(Price)>=150;

"15. Select the name and price of the cheapest product. -> With Nested"
SELECT Name,Price FROM Products WHERE Price = (SELECT MIN(Price) FROM Products);

"16. Select the name of each manufacturer along with the name and price of its most expensive product."
SELECT Products.Name AS Product_Name ,Manufacturers.Name AS Manufacturers_NAME,Products.Price AS Price_Range from Products INNER JOIN Manufacturers 
ON products.manufacturer = Manufacturers.Code AND Products.Price = (SELECT MAX(Price) FROM Products WHERE products.manufacturer = Manufacturers.Code)

"17. Select the name of each manufacturer which have an average price above $145 and contain at least 2 different products."
SELECT m.Name, AVG(p.Price) AS P_Price, COUNT(p.manufacturer) AS M_COunt
FROM Manufacturers m, Products p 
WHERE p.Manufacturer = m.code GROUP BY p.Manufacturer HAVING p_price >= 150 and m_count >= 2;

"18. Add a new product: Loudspeakers, $70, manufacturer 2."
 INSERT INTO Products( Code, Name , Price , Manufacturer)
 VALUES ( 11, 'Loudspeakers' , 70 , 2 ); 
 
"19. Update the name of product 8 to Laser Printer."
UPDATE Products SET Name = 'Laser Printer' WHERE Code = 8;

"20. Apply a 10% discount to all products."
UPDATE Products SET Price = Price - (Price * 0.1);

"21. Apply a 10% discount to all products with a price larger than or equal to $120."
UPDATE Products SET Price = Price - (Price * 0.1) WHERE Price >= 120;

