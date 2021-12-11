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