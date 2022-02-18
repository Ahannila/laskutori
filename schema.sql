CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE Post (
    id SERIAL PRIMARY KEY,
    content TEXT,
    price INTEGER,
    creator_id INTEGER REFERENCES Users,
    sent_at TIMESTAMP,
    visible INTEGER,
    title TEXT,
    category TEXT REFERENCES Category
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
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    kuvat TEXT
);

CREATE TABLE Favourites(
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    post_id INTEGER REFERENCES post
);

CREATE TABLE Category(
    id SERIAL PRIMARY KEY,
    category TEXT,
    post_id INTEGER REFERENCES post
    );


    --taulukkoja ovat USERS, ADMINS, POSTS, FAVORITES, CATEGORIES, COMMENTS, PICTURES
    --Post taulukkoon pitää lisätä hinta!!!!!!!!!!!
