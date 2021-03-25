// Music Analytics on Graph Database
// Santos Borom 2021
// License: Creative Commons License
// musical character is for genres

CREATE CONSTRAINT ON (g:Styles) ASSERT g.genres IS UNIQUE;

CALL apoc.periodic.iterate(
"CALL apoc.load.csv('file:///data_by_genres.csv', {headers: true} )
    YIELD map AS row RETURN row",
    "WITH toString(row.genres) AS genres,
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

    MERGE (h:Styles {
        genres: genres
    })
    ON CREATE SET h.popularity = popularity, h.valence = valence, h.acousticness = acousticness, h.danceability = danceability, h.energy = energy, h.instrumentalness = instrumentalness, h.loudness = loudness, h.liveness = liveness, h.speechiness = speechiness, h.tempo = tempo, h.key = key, h.mode = mode, h.duration_ms = duration_ms
      ",
{batchSize: 5000}
)
