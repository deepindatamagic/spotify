// Music Analytics on Graph Database
// Santos Borom 2021
// License: Creative Commons License
// musical character is for the track

// constraints
CREATE CONSTRAINT ON (track:Songs)  ASSERT track.id IS UNIQUE;
CREATE CONSTRAINT ON (arts:Artists) ASSERT arts.artists IS UNIQUE;


CALL apoc.periodic.iterate(
"CALL apoc.load.csv('file:///data.csv', {headers: true} )
 YIELD map AS row RETURN row",
 "WITH row.id as id, toInteger(row.year) AS year, toFloat(row.valence) AS valence,
    toFloat(row.acousticness) AS acousticness, toFloat(row.danceability) AS danceability,
    toFloat(row.energy) AS energy, toFloat(row.instrumentalness) AS instrumentalness,
    toFloat(row.loudness) AS loudness, toFloat(row.liveness) AS liveness,
    toInteger(row.popularity) AS popularity, toFloat(row.speechiness) AS speechiness,
    toFloat(row.tempo) AS tempo, toInteger(row.mode) AS mode, toInteger(row.Explicit) AS explicit,
    toInteger(row.release_date) AS release_date, row.name AS name, row.artists AS artists,
    toInteger(row.key) AS key   
    
    MERGE (track:Songs {id:id})
    ON CREATE SET track.id = id, track.artists = artists,
    track.name = name, track.popularity = popularity, track.year = year,
    track.valence = valence, track.acousticness = acousticness, track.energy = energy,
    track.danceability = danceability, track.instrumentalness = instrumentalness,
    track.loudness = loudness, track.liveness = liveness, track.speechiness  = speechiness,
    track.tempo = tempo, track.mode = mode, track.explicit = explicit,
    track.release_date = release_date, track.key = key

    MERGE (art:Artists {
        artists: artists
        })
    CREATE (art)-[:ACTS]->(track)
    
    MERGE (y:Years {
        year: track.year
        })
    CREATE (track)-[:RELEASED]->(y)
      ",
{batchSize: 5000}
)