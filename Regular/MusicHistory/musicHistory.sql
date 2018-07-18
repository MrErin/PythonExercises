-- Query all of the entries in the Genre table

select *
from Genre

-- Using the INSERT statement, add one of your favorite artists to the Artist table.

insert into Artist
    (ArtistId, ArtistName, YearEstablished)
values
    (28, 'New Artist', 1911)

-- Using the INSERT statement, add one, or more, albums by your artist to the Album table.

insert into Album
    (Title, ReleaseDate, AlbumLength, Label, ArtistId, GenreId)
values
    ('The First Album', 1911, 22, 'A Label', 28, 4)

-- Using the INSERT statement, add some songs that are on that album to the Song table.

insert into Song
    (Title, SongLength, ReleaseDate, GenreId, ArtistId, AlbumId)
values
    ('Song One', 55, 1911, 4, 28, 23),
    ('Song Two', 55, 1911, 4, 28, 23)

-- Write a SELECT query that provides the song titles, album title, and artist name for all of the data you just entered in. Use the LEFT JOIN keyword sequence to connect the tables, and the WHERE keyword to filter the results to the album and artist you added.

select a.ArtistName, b.Title, s.Title
from Artist a
    left join Album b on a.ArtistId = b.ArtistId
    left join song s on a.ArtistId = s.ArtistId
where a.ArtistId = 28

-- Write a SELECT statement to display how many songs exist for each album. You'll need to use the COUNT() function and the GROUP BY keyword sequence.

select b.Title, count(s.SongId) 'SongCount'
from Album b
    join Song s on s.AlbumId = b.AlbumId
group by b.Title

-- Write a SELECT statement to display how many songs exist for each artist. You'll need to use the COUNT() function and the GROUP BY keyword sequence.

select a.ArtistName, count(s.SongId) 'SongCount'
from Artist a
    join Song s on a.ArtistId = s.ArtistId
group by a.ArtistName

-- Write a SELECT statement to display how many songs exist for each genre. You'll need to use the COUNT() function and the GROUP BY keyword sequence.

select g.Label 'Genre', count(s.SongId) 'SongCount'
from Genre g
    join Song s on s.GenreId = g.GenreId
group by g.Label

-- Using MAX() function, write a select statement to find the album with the longest duration. The result should display the album title and the duration.

select b.Title, max(b.AlbumLength) 'Length'
from Album b

-- Using MAX() function, write a select statement to find the song with the longest duration. The result should display the song title and the duration.

select s.Title, max(s.SongLength) 'SongLength'
from Song s

-- Modify the previous query to also display the title of the album.

select b.Title 'AlbumTitle', s.Title 'SongTitle', max(s.SongLength) 'SongLength'
from Song s
    join Album b on s.AlbumId = b.AlbumId