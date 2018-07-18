create table "Superhero" (
    "Superhero_ID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "Name" TEXT NOT NULL,
    "Gender" TEXT  NOT NULL,
    "Secret_ID" TEXT NOT NULL,
    "Affiliation_ID" TEXT,
    FOREIGN KEY
("Affiliation_ID") REFERENCES "Affiliation"
("Affiliation_ID")

)

insert into Superhero
values(null, 'Green Lantern', 'M', 'Hal Jordan')
insert into Superhero
values(null, 'Wonder Woman', 'F', 'Diana Prince')
insert into Superhero
values(null, 'Batman', 'M', 'Bruce Wayne')

create table "Sidekick"(
    "Sidekick_ID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "Name" TEXT NOT NULL,
    "Gender" TEXT NOT NULL,
    "Profession" TEXT NOT NULL,
    "Superhero_ID" INTEGER NOT NULL,
    FOREIGN KEY
("Superhero_ID") REFERENCES "Superhero"
("Superhero_ID")
)