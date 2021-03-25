// Music Analytics on Graph Database
// Santos Borom 2021
// License: Creative Commons License
//musical character is for artists

CREATE CONSTRAINT ON (art:Arts)  ASSERT art.artists IS UNIQUE;
CREATE CONSTRAINT ON (g:Genres) ASSERT g.genres IS UNIQUE;

CALL apoc.periodic.iterate(
"CALL apoc.load.csv('file:///data_w_genres.csv', {headers: true} )
    YIELD map AS row",
    "WITH apoc.convert.fromJsonList(row.genres) AS genres,
    toString(row.artists) AS artists,
    toFloat(row.popularity) AS popularity,
    toFloat(row.valence) AS valence,
    toFloat(row.acousticness) AS acousticness,
    toFloat(row.danceability) AS danceability,
    toFloat(row.energy) AS energy,
    toFloat(row.instrumentalness) AS instrumentalness,
    toFloat(row.loudness) AS loudness,
    toFloat(row.liveness) AS liveness,
    toFloat(row.speechiness) AS speechiness,
    toFloat(row.tempo) AS tempo,
    toInteger(row.mode) AS mode,
    toInteger(row.key) AS key,
    toFloat(row.duration_ms) AS duration_ms

    MERGE (art:Arts {artists:artists})
    
    ON CREATE SET art.popularity = popularity,
    art.genres = genres, art.danceability = danceability, art.energy = energy, art.instrumentalness = instrumentalness, art.loudness = loudness, art.speechiness = speechiness, art.tempo = tempo, art.liveness = liveness, art.key = key, art.acousticness = acousticness, art.mode = mode, art.valence = valence, art.duration_ms = duration_ms

    WITH art AS a
    UNWIND a.genres AS gen
    MERGE (g:Genres {genres:gen})
    CREATE (a)-[r:STYLE]->(g)
    ",
{batchSize: 5000}
)




