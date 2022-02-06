CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE Post (
    id SERIAL PRIMARY KEY,
    content TEXT,
    creator_id INTEGER REFERENCES Users,
    sent_at TIMESTAMP,
    visible INTEGER
);

CREATE TABLE Comments (
    id SERIAL PRIMARY KEY,
    post_id INTEGER REFERENCES Post,
    user_id INTEGER REFERENCES Users,
    comment TEXT,
    sent_at TIMESTAMP
);

CREATE TABLE Admins(
    id SERIAL PRIMARY KEY,
    rights INTEGER,
    username TEXT UNIQUE,
    password TEXT
);
    

CREATE TABLE photos (
    id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    kuvat TEXT
);


    --taulukkoja ovat USERS, ADMINS, POSTS, FAVORITES, CATEGORIES, COMMENTS, PICTURES
