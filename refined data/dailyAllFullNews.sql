SELECT DISTINCT newsID, REPLACE(newsTitle, '�', '') AS newsTitle, Date, fullText
FROM "newsFull"
    INNER JOIN "ARTICLE1"
    ON "newsID1" = "newsID"

UNION

SELECT DISTINCT newsID, REPLACE(newsTitle, '�', '') AS newsTitle, Date, fullText
FROM "newsFull"
    INNER JOIN "ARTICLE2"
    ON "newsID2" = "newsID"

UNION

SELECT DISTINCT newsID, REPLACE(newsTitle, '�', '') AS newsTitle, Date, fullText
FROM "newsFull"
    INNER JOIN "ARTICLE3"
    ON "newsID3" = "newsID"

UNION

SELECT DISTINCT newsID, REPLACE(newsTitle, '�', '') AS newsTitle, Date, fullText
FROM "newsFull"
    INNER JOIN "ARTICLE4"
    ON "newsID4" = "newsID"

UNION

SELECT DISTINCT newsID, REPLACE(newsTitle, '�', '') AS newsTitle, Date, fullText
FROM "newsFull"
    INNER JOIN "ARTICLE5"
    ON "newsID5" = "newsID"

UNION

SELECT DISTINCT newsID, REPLACE(newsTitle, '�', '') AS newsTitle, Date, fullText
FROM "newsFull"
    INNER JOIN "ARTICLE6"
    ON "newsID6" = "newsID"

UNION

SELECT DISTINCT newsID, REPLACE(newsTitle, '�', '') AS newsTitle, Date, fullText
FROM "newsFull"
    INNER JOIN "ARTICLE7"
    ON "newsID7" = "newsID"

UNION

SELECT DISTINCT newsID, REPLACE(newsTitle, '�', '') AS newsTitle, Date, fullText
FROM "newsFull"
    INNER JOIN "ARTICLE7"
    ON "newsID7" = "newsID"

UNION

SELECT DISTINCT newsID, REPLACE(newsTitle, '�', '') AS newsTitle, Date, fullText
FROM "newsFull"
    INNER JOIN "ARTICLE8"
    ON "newsID8" = "newsID"


UNION

SELECT DISTINCT newsID, REPLACE(newsTitle, '�', '') AS newsTitle, Date, fullText
FROM "newsFull"
    INNER JOIN "ARTICLE9"
    ON "newsID9" = "newsID"

UNION

SELECT DISTINCT newsID, REPLACE(newsTitle, '�', '') AS newsTitle, Date, fullText
FROM "newsFull"
    INNER JOIN "ARTICLE10"
    ON "newsID10" = "newsID"