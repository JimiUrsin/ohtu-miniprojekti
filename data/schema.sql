CREATE TABLE if not exists Recommendations
(
    id INTEGER PRIMARY KEY,
    title TEXT,
    type TEXT,
    url TEXT
);

CREATE TABLE if not exists Authors
(
    id INTEGER PRIMARY KEY,
    recom_id INTEGER REFERENCES Recommendations(id),
    author TEXT
)