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

CREATE TABLE if not exists Authors
(
    id INTEGER PRIMARY KEY,
    recom_id INTEGER REFERENCES Recommendations(id),
    author TEXT
)