// Music Analytics on Graph Database
// Santos Borom 2021
// License: Creative Commons License

CALL db.constraints

CALL db.indexes();

MATCH (a:Arts)
UNWIND a.genres  AS gene
RETURN a
LIMIT 10

// delete nodes
CALL apoc.periodic.iterate(
  'MATCH (a:Arts) RETURN a',
  'DETACH DELETE a',
  { batchSize:500 }
)

// returns all artists
MATCH (a:Arts) 
UNWIND a.artists AS actors
RETURN actors

UNWIND ['asian american hip hop', 'cali rap', 'west coast trap'] AS x
MERGE (n:Genres  {genres:x})

// will not match
WITH ['Sergei Rachmaninoff', 'James Levine', 'Berliner Philharmoniker'] AS names
MATCH (a:Artists)
WHERE a.artists IN names
RETURN a

// simple unwind
WITH ['Sergei Rachmaninoff', 'James Levine', 'Berliner Philharmoniker'] AS actors
UNWIND actors AS people
RETURN people

// wont match
WITH ['THE GUY'] AS name
MATCH (a:Artists)
WHERE a.artists IN name
RETURN a

// will match since string
WITH "['THE GUY']" as cast
MATCH (m:Artists)-[r:ACTS]->(n:Songs)
WHERE m.artists = cast
RETURN m,n

WITH ['Sergei Rachmaninoff', 'James Levine', 'Berliner Philharmoniker'] AS names1,
['Sergei Rachmaninoff', 'James Levine'] AS names2
RETURN [n IN names1 WHERE n in names2] as names

WITH ['Sergei Rachmaninoff', 'James Levine', 'Berliner Philharmoniker'] AS names
MATCH (n:Artists)
UNWIND n.artists AS people
RETURN  DISTINCT [people IN names]


WITH ['comedy rock', 'comic', 'parody'] AS genres
UNWIND genres AS g
RETURN g

WITH ['Andrew Lloyd Webber', '"Cats" 1981 Original London Cast', 'Elaine Paige'] as casts
UNWIND casts as people
RETURN people



MATCH (a:Artists)
UNWIND a.artists AS people
RETURN a, people
LIMIT 10


// will not match but returns everyone
WITH ['Andrew Lloyd Webber', '"Cats" 1981 Original London Cast', 'Elaine Paige'] as casts
UNWIND casts as people
MATCH (a:Artists)
WHERE [a.artists IN casts]
RETURN a


WITH ['Andrew Lloyd Webber', '"Cats" 1981 Original London Cast', 'Elaine Paige'] as casts
MATCH (a:Artists)
UNWIND a.artists  AS people
RETURN DISTINCT [people IN casts]


// will not match
WITH ['Andrew Lloyd Webber', '"Cats" 1981 Original London Cast', 'Elaine Paige'] as casts
MATCH (a:Artists)
UNWIND a.artists  AS people
RETURN people = casts

// will not match
WITH ['Andrew Lloyd Webber', '"Cats" 1981 Original London Cast', 'Elaine Paige'] as casts
MATCH (a:Artists)
UNWIND a.artists  AS people
RETURN people = casts

// wont match
WITH ["'Cats' 1981 Original London Cast"] AS casts
MATCH (a:Artist)
UNWIND a.artist AS people
RETURN [cast in people]

// wont match
WITH ["Cats 1981 Original London Cast"] as casts
MATCH (a:Artist)
WHERE a.artists =  casts
RETURN a

// matches
WITH ["'Cats' 1983 Broadway Cast"] as casts
UNWIND casts AS actors
MATCH (a:Arts)
WHERE a.artists =  actors
RETURN a

// will not match
WITH ["'Cats' 1983 Broadway Cast"] as casts
UNWIND casts AS actors
MATCH (a:Artists)
UNWIND a AS arts
RETURN arts = actors
LIMIT 2

// will unwind
MATCH (g:Genres)
UNWIND g AS genres
RETURN genres
LIMIT 10

MATCH (a:ArtistTmp),(b:Arts)
WHERE a.artists = b.artists
RETURN a,b
LIMIT 10

MATCH (a:Arts)
WHERE a.artists ='Frank Parker'
RETURN a


MATCH (a:ArtistsTmp)
WITH a.artists AS artists
RETURN artists
LIMIT 5

MATCH (a:ArtistsTmp)
WITH a.artists AS artists
UNWIND artists AS arts
RETURN arts
LIMIT 5

// (:ArtistsTmp) contains the names and has songs and years relationships
// (:Arts) contains musical character and names  and has genres relationships
MATCH (a:ArtistsTmp)
WITH a.artists AS artists, a
UNWIND artists AS actors
WITH actors, a
MATCH  (b:Arts)
WHERE b.artists = actors
RETURN actors, a AS performers, b AS artist
LIMIT 10

// otherway around do not work
// since the artists needs to be unwound
MATCH (a:Arts)
WITH a.artists AS artists
UNWIND artists AS actors
WITH actors
MATCH (b:ArtistsTmp)
WHERE b.artists = actors
RETURN b, actors
LIMIT 10

MATCH (a:Arts)
WHERE a.artists = 'Sergei Rachmaninoff'
RETURN a

// rename (:ArtistsTmp)
MATCH (a:ArtistsTmp)
WITH collect(a) as nodes
CALL apoc.refactor.rename.label("ArtistsTmp", "Performers", nodes)
YIELD committedOperations
RETURN committedOperations


// delete nodes
CALL apoc.periodic.iterate(
  'MATCH (a:ArtistsTmp) RETURN a',
  'DETACH DELETE a',
  { batchSize:500 }
)

DROP CONSTRAINT ON (arts:ArtistsTmp) ASSERT arts.artists IS UNIQUE;
CREATE CONSTRAINT ON (p:Performers) ASSERT p.artists IS UNIQUE;


MATCH (a:Arts)
WITH collect(a) as nodes
CALL apoc.refactor.rename.label("Arts", "Artists", nodes)
YIELD committedOperations
RETURN committedOperations

DROP CONSTRAINT ON (art:Arts)  ASSERT art.artists IS UNIQUE;









