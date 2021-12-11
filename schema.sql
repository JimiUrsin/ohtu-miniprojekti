CREATE TABLE if not exists Recommendations
(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    type TEXT NOT NULL,
    url TEXT,
    isbn TEXT,
    description TEXT,
    comment TEXT
);

CREATE TABLE if not exists AuthorRecommendations
(
    recom_id INTEGER REFERENCES Recommendations(id) NOT NULL,
    author_id INTEGER REFERENCES Authors(id) NOT NULL
);

CREATE TABLE if not exists Authors
(
    id INTEGER PRIMARY KEY,
    author TEXT
);

CREATE TRIGGER DeleteAuthorConnectionWithRecommendation
AFTER DELETE ON Recommendations
BEGIN
    DELETE FROM AuthorRecommendations WHERE recom_id = OLD.id;
END;

CREATE TRIGGER DeleteAuthorWithLastRecommendation
AFTER DELETE ON AuthorRecommendations
WHEN NOT EXISTS (SELECT 1 FROM AuthorRecommendations WHERE author_id = OLD.author_id)
BEGIN
    DELETE FROM Authors WHERE id = OLD.author_id;
END;