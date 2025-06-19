-- SQLite
-- database: newFullClean.db
-- Highlight, Right-Click, and Press "Run Query"
-- Use the Database on file
SELECT DISTINCT newsID, REPLACE(fullText, '�', '') AS fullTextC FROM "newsFull";