--usuario dado su identificador
SELECT id, username, email, name, bio, password FROM "User" WHERE id = ?;
--// Esta consultas es lo mismo que SELECT * FROM "User" WHERE id = ?;
--// pero te la pongo asi por si tuvieras que sacar solo un parametro

--Lista de usuarios que sigue el usuario dado
SELECT u.id, u.username, u.email, u.name, u.bio, u.password FROM "User" u, follower f WHERE u.id = f.followedid AND f.userid = ? LIMIT ?;

--Lista de usuarios que siguen a un usuario dado
SELECT u.id, u.username, u.email, u.name, u.bio, u.password FROM "User" u, follower f WHERE u.id = f.userid AND f.followedid = ? LIMIT ?;

--Listas de playLists de un usuario dado
SELECT id, name, userid, creationdate, description FROM list WHERE userid = ? LIMIT ?;

--Lista de playLists dado su id
SELECT id, name, userid, creationdate, description FROM list WHERE id = ?;

--Objener imagen de un album dado su identificador
SELECT image FROM album WHERE id = ?;

--Obtener imagen de una cancion dado su identificador
SELECT a.image FROM album a, song s WHERE a.id = s.albumid AND s.id = ?;

-- Obtener fichero de audio de una cancion dado un id
SELECT file FROM song WHERE id = ?;

--Obtener albunes dado año de lanzamiento
SELECT id, name, groupid, publishdate, description, image FROM album WHERE EXTRACT(YEAR FROM publishdate) = ? LIMIT ?;

-- Obtener albunes dado un nombre
SELECT id, name, groupid, publishdate, description, image FROM album WHERE name = ?;

-- Obtener lista de albunes dado un autor
SELECT a.id, a.name, a.groupid, a.publishdate, a.description, a.image FROM album a, components c, "Group" g WHERE a.groupid = g.id AND g.id = c.groupid AND c.artistid = ? LIMIT ?;

--Lista de canciones de una playList
SELECT c.id, c.name, c.genre, c.file, c.lenght, c.groupid, c.albumid FROM song c, list l, listsong ls WHERE c.id = ls.songid AND ls.listid = l.id AND l.id = ? LIMIT ?;

--Lista de canciones dado un genero
SELECT id, name, genre, file, lenght, groupid, albumid FROM song WHERE genre = ? LIMIT ?;

--Lista de canciones dado el id de un autor
SELECT c.id, c.name, c.genre, c.file, c.lenght, c.groupid, c.albumid
FROM song c, "Group" g, components cp, artist a
WHERE c.groupid = g.id AND g.id = cp.groupid AND cp.artistid = a.id AND a.id = ? LIMIT ?;

--Lista de canciones dado un grupo
SELECT c.id, c.name, c.genre, c.file, c.lenght, c.groupid, c.albumid
FROM song c, "Group" g, components cp, artist a
WHERE c.groupid = g.id AND g.id = ? LIMIT ?;

--Lista de autores dado el nombre
SELECT id, name, bio FROM artist WHERE name = ? LIMIT ?;

-- Lista de usuarios dado parametros
SELECT id, username, email, name, bio, password FROM "User"x WHERE name = ? OR username = ? LIMIT ?;
