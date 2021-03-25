// Music Analytics on Graph Database
// Santos Borom 2021
// License: Creative Commons License
// musical character is for artists

// loads data_by_artists and creates temp nodes
CALL apoc.periodic.iterate(
"CALL apoc.load.csv('file:///data_by_artist.csv', {headers: true} )
    YIELD map AS row RETURN row",
    "WITH toFloat(row.valence) AS valence, toFloat(row.acousticness) AS acousticness, 
        toFloat(row.danceability) AS danceability, 
        toFloat(row.energy) AS energy, 
        toFloat(row.instrumentalness) AS instrumentalness,
        toFloat(row.loudness) AS loudness, 
        toFloat(row.liveness) AS liveness,
        toInteger(row.popularity) AS popularity, 
        toFloat(row.speechiness) AS speechiness,
        toFloat(row.tempo) AS tempo, toInteger(row.mode) AS mode, toInteger(row.Explicit) AS explicit,
        row.artists AS artists, toInteger(row.key) AS key   

    MERGE (art:ArtsData {
        artists: artists
        })
    ON CREATE SET art.popularity = popularity,
    art.danceability = danceability, art.energy = energy, 
    art.instrumentalness = instrumentalness, art.loudness = loudness, art.speechiness = speechiness, art.tempo = tempo,
    art.liveness = liveness, art.explicit = explicit,
    art.key = key, art.acousticness = acousticness, 
    art.mode = mode, art.valence = valence

    MATCH (a:Artists),(b:ArtsData)
    WHERE a.artists =  b.artists
    SET a.danceability = b.danceability, 
    a.energy = b.energy, 
    a.instrumentalness = b.instrumentalness, 
    a.loudness = b.loudness, 
    a.speechiness = b.speechiness, 
    a.tempo = b.tempo,
    a.liveness = b.liveness, 
    a.explicit = b.explicit,
    a.key = b.key, 
    a.acousticness = b.acousticness, 
    a.mode = b.mode, 
    a.valence = b.valence

    MATCH (n:ArtsData) DELETE n
    ",
{batchSize: 1000}
)