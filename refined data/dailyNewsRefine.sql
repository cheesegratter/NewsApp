-- SQLite
-- database: newFullClean.db
-- Highlight, Right-Click, and Press "Run Query"
-- Use the Database on file
SELECT DISTINCT DATE, 
newsID1, REPLACE(newsTitle1, '�', '') AS newsTitle1, 
newsID2, REPLACE(newsTitle2, '�', '') AS newsTitle2,
newsID3, REPLACE(newsTitle3, '�', '') AS newsTitle3,
newsID4, REPLACE(newsTitle4, '�', '') AS newsTitle4,
newsID5, REPLACE(newsTitle5, '�', '') AS newsTitle5,
newsID6, REPLACE(newsTitle6, '�', '') AS newsTitle6,
newsID7, REPLACE(newsTitle7, '�', '') AS newsTitle7,
newsID8, REPLACE(newsTitle8, '�', '') AS newsTitle8,
newsID9, REPLACE(newsTitle9, '�', '') AS newsTitle9,
newsID10, REPLACE(newsTitle10, '�', '') AS newsTitle10
FROM dailyNewsClean;