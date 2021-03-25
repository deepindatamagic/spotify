// Music Analytics on Graph Database
// Santos Borom 2021
// License: Creative Commons License

CREATE CONSTRAINT ON (y:YearsTmp) ASSERT y.year IS UNIQUE;

// musical character is for year
CALL apoc.load.csv('file:///data_by_year.csv', {headers: true} )
    YIELD map AS row
    WITH toString(row.year) AS year,
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
    toInteger(row.key) AS key

    MERGE (y:YearsTmp {
        year: year
    })    
    ON CREATE SET y.popularity = popularity, y.valence = valence, y.acousticness = acousticness, y.danceability = danceability, y.energy = energy, y.instrumentalness = instrumentalness, y.liveness = liveness, y.loudness = loudness, y.speechiness = speechiness, y.tempo = tempo, y.key = key, y.mode = mode