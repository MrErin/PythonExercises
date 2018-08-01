-- `playlists_track_count.sql`: Provide a query that shows the total number of tracks in each playlist. The Playlist name should be include on the resulant table.

SELECT l.Name as 'PlaylistName', COUNT(t.TrackId) as 'NumberOfTracks'

FROM Playlist l
    JOIN PlaylistTrack t on l.PlaylistId = t.PlaylistId

GROUP BY l.name