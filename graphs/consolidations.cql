// Music Analytics on Graph Database
// Santos Borom 2021
// License: Creative Commons License

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
CALL apoc.refactor.rename.label("ArtistsTmp", "Musicians", nodes)
YIELD committedOperations
RETURN committedOperations

// delete nodes
CALL apoc.periodic.iterate(
  'MATCH (a:ArtistsTmp) RETURN a',
  'DETACH DELETE a',
  { batchSize:500 }
)

DROP CONSTRAINT ON (arts:ArtistsTmp) ASSERT arts.artists IS UNIQUE;
CREATE CONSTRAINT ON (p:Musicians) ASSERT p.artists IS UNIQUE;

MATCH (a:Arts)
WITH collect(a) as nodes
CALL apoc.refactor.rename.label("Arts", "Artists", nodes)
YIELD committedOperations
RETURN committedOperations

DROP CONSTRAINT ON (art:Arts)  ASSERT art.artists IS UNIQUE;
CREATE CONSTRAINT ON (art:Artists)  ASSERT art.artists IS UNIQUE;

// (:ArtistsTmp) contains the names and has songs and years relationships
// (:Arts) contains musical character and names  and has genres relationships
MATCH (a:Musicians)
WITH a.artists AS artists, a AS pnodes
UNWIND artists AS actors
WITH pnodes, actors
MATCH  (b:Artists)
WHERE b.artists = actors
RETURN actors, pnodes AS musicians, b AS artist
LIMIT 10

// extremely slow
MATCH (p:Musicians),(b:Artists)
WITH p.artists AS artists, p, b
UNWIND artists AS actors
WITH p, actors, b
WHERE b.artists = actors
WITH p, actors, b
CREATE (p)-[:PERFORMER]->(b)
RETURN p,b

CALL apoc.periodic.iterate(
  "MATCH (p:Musicians),(b:Artists)
  WITH p.artists AS artists, p, b
  UNWIND artists AS actors
  WITH p, actors, b
  WHERE b.artists = actors
  WITH p, actors, b
  RETURN p,b,actors",
  "CREATE (p)-[:PERFORMER]->(b)",
  {batchSize:1000})


// genres
MATCH (n:Genres)
UNWIND n.genre AS genre
RETURN genre
LIMIT 5

// rename genre property of (:Genres) to plural
MATCH (n:Genres)
WITH collect(n) AS genes
CALL apoc.refactor.rename.nodeProperty("genre", "genres", genes)
YIELD batches, total, timeTaken, committedOperations
RETURN batches, total, timeTaken, committedOperations

MATCH (m:Genres),(n:Styles)
WITH m.genres AS mgen, n.genres  AS ngen
UNWIND mgen AS genres
WITH genres, ngen
WHERE genres = ngen
RETURN genres, ngen
LIMIT 5

MATCH (m:Genres),(n:Styles)
WITH m,n, m.genres AS mgen, n.genres  AS ngen
UNWIND mgen AS genres
WITH genres, ngen, m,n
WHERE genres = ngen
RETURN m,n
LIMIT 5

// clone (:Genres)
MATCH (m:Genres),(n:Styles)
SET m = n
RETURN m

MATCH (m:Genres)<-[r:STYLE]-(n:Artists)
RETURN m,n
LIMIT 5

MATCH (m:Genres)<-[r:STYLE]-(n:Artists)
WITH m.genres AS genres, m, n
MATCH (s:Styles)
WHERE s.genres = genres
CREATE (n)-[r:STYLE]->(s)
RETURN s

CALL apoc.periodic.iterate(
  'MATCH (m:Genres) RETURN m',
  'DETACH DELETE m',
  { batchSize:500 }
)

DROP CONSTRAINT ON (g:Genres) ASSERT g.genres IS UNIQUE;

// alternative approach
// merge (:Styles) into (:Genres)
MATCH (m:Genres),(n:Styles)
WITH m,n, m.genres AS mgen, n.genres  AS ngen
UNWIND mgen AS genres
WITH m,n, genres, ngen
WHERE genres = ngen
WITH head(collect([m,n])) AS nodes, m,n, genres, ngen
CALL apoc.refactor.mergeNodes(nodes, {properties:"combine", mergeRels:true})
YIELD node
RETURN node

// rename (:Styles) to (:Genres)
MATCH (s:Styles)
WITH collect(s) as nodes
CALL apoc.refactor.rename.label("Styles", "Genres", nodes)
YIELD committedOperations
RETURN committedOperations

// ensure constraints
CREATE CONSTRAINT ON (g:Genres) ASSERT g.genres IS UNIQUE;

CALL apoc.periodic.iterate(
  'MATCH (s:Styles) RETURN s',
  'DETACH DELETE s',
  { batchSize:500 }
)

DROP CONSTRAINT ON (s:Styles) ASSERT s.genres IS UNIQUE;

MATCH (u:Years), (v:YearsTmp)
WHERE u.year = v.year
RETURN u,v
LIMIT 5

MATCH (u:Years), (v:YearsTmp)
WHERE u.year = v.year
SET u = v
RETURN u,v

CALL apoc.periodic.iterate(
  'MATCH (y:YearsTmp) RETURN y',
  'DETACH DELETE y',
  { batchSize:100 }
)

DROP CONSTRAINT ON (y:YearsTmp) ASSERT y.year IS UNIQUE;

// rename (:Styles) to (:Genres)
MATCH (a:Artists)
WITH collect(a) as nodes
CALL apoc.refactor.rename.label("Artists", "Artist", nodes)
YIELD committedOperations
RETURN committedOperations

CALL apoc.periodic.iterate(
  'MATCH (a:Artists) RETURN a',
  'DETACH DELETE a',
  { batchSize:100 }
)

DROP CONSTRAINT ON (a:Artists) ASSERT a.artists IS UNIQUE;
