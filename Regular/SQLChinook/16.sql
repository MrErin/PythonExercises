-- `tracks_no_id.sql`: Provide a query that shows all the Tracks, but displays no IDs. The result should include the Album name, Media type and Genre.

SELECT t.Name as 'TrackName', b.Title as 'AlbumName', m.Name as 'MediaType', g.Name as 'Genre'

FROM Track t

    JOIN Album b on t.AlbumId = b.AlbumId

    JOIN MediaType m on m.MediaTypeId = t.MediaTypeId

    JOIN Genre g on t.GenreId = g.GenreId