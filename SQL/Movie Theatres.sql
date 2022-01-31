 "Create Tables"
 CREATE TABLE Movies (
   Code INTEGER PRIMARY KEY NOT NULL,
   Title TEXT NOT NULL,
   Rating TEXT 
 );
 
 CREATE TABLE MovieTheaters (
   Code INTEGER PRIMARY KEY NOT NULL,
   Name TEXT NOT NULL,
   Movie INTEGER  
     CONSTRAINT fk_Movies_Code REFERENCES Movies(Code)
 );
"Insert the Data"
 
 INSERT INTO Movies(Code,Title,Rating) VALUES(9,'Citizen King','G');
 INSERT INTO Movies(Code,Title,Rating) VALUES(1,'Citizen Kane','PG');
 INSERT INTO Movies(Code,Title,Rating) VALUES(2,'Singin'' in the Rain','G');
 INSERT INTO Movies(Code,Title,Rating) VALUES(3,'The Wizard of Oz','G');
 INSERT INTO Movies(Code,Title,Rating) VALUES(4,'The Quiet Man',NULL);
 INSERT INTO Movies(Code,Title,Rating) VALUES(5,'North by Northwest',NULL);
 INSERT INTO Movies(Code,Title,Rating) VALUES(6,'The Last Tango in Paris','NC-17');
 INSERT INTO Movies(Code,Title,Rating) VALUES(7,'Some Like it Hot','PG-13');
 INSERT INTO Movies(Code,Title,Rating) VALUES(8,'A Night at the Opera',NULL);
 
 INSERT INTO MovieTheaters(Code,Name,Movie) VALUES(1,'Odeon',5);
 INSERT INTO MovieTheaters(Code,Name,Movie) VALUES(2,'Imperial',1);
 INSERT INTO MovieTheaters(Code,Name,Movie) VALUES(3,'Majestic',NULL);
 INSERT INTO MovieTheaters(Code,Name,Movie) VALUES(4,'Royale',6);
 INSERT INTO MovieTheaters(Code,Name,Movie) VALUES(5,'Paraiso',3);
 INSERT INTO MovieTheaters(Code,Name,Movie) VALUES(6,'Nickelodeon',NULL);

"1. Select the title of all movies."
SELECT Title FROM Movies;

"2. Show all the distinct ratings in the database."
SELECT DISTINCT (Rating) FROM Movies;

"3. Show all unrated movies."
SELECT * FROM Movies WHERE Rating IS NULL;

"4. Select all movie theaters that are not currently showing a movie."
SELECT * FROM MovieTheaters WHERE Movie is NULL;

"5. Select all data from all movie theaters and, additionally, the data from the movie that is being shown in the theater (if one is being shown)."
 SELECT * FROM MovieTheaters LEFT JOIN Movies ON MovieTheaters.Movie = Movies.Code;

"6. Select all data from all movies and, if that movie is being shown in a theater, show the data from the theater."
 SELECT * FROM MovieTheaters RIGHT JOIN Movies ON MovieTheaters.Movie = Movies.Code;

"7. Show the titles of movies not currently being shown in any theaters."
 /* With JOIN */
 SELECT Movies.Title FROM MovieTheaters RIGHT JOIN Movies ON MovieTheaters.Movie = Movies.Code WHERE MovieTheaters.Movie IS NULL;

/* With subquery */
SELECT Title FROM Movies WHERE Code NOT IN( SELECT Movie FROM MovieTheaters WHERE Movie IS NOT NULL);

"8. Add the unrated movie One, Two, Three."
INSERT INTO Movies(Title,Rating) VALUES('One, Two, Three',NULL);

"9. Set the rating of all unrated movies to G."
 UPDATE Movies SET Rating='G' WHERE Rating IS NULL;

"10. Remove movie theaters projecting movies rated NC-17".
DELETE FROM MovieTheaters WHERE Movie IN (SELECT Code FROM Movies WHERE Rating = 'NC-17');

