-- usuarios

SELECT insert_new_user('A','alice@mail.net','Alice','ApassA');
SELECT make_admin(1);
SELECT insert_new_user('B','bob@mail.net','Bob','BpassB');
SELECT insert_new_user('C','charlie@mail.net','Charlie','CpassC');
SELECT insert_new_user('D','dario@mail.net','Dario','DpassD');

-- artista
SELECT insert_new_artist('Soundatelier', 'Descripcion vacia', bytea_import('/usr/src/datosPoblar/artistas/def.png'));
SELECT insert_new_artist('The moose', 'Descripcion vacia', bytea_import('/usr/src/datosPoblar/artistas/def.png'));
SELECT insert_new_artist('2Invention', 'Descripcion vacia', bytea_import('/usr/src/datosPoblar/artistas/def.png'));
SELECT insert_new_artist('Addict sound', 'Descripcion vacia', bytea_import('/usr/src/datosPoblar/artistas/def.png'));

-- album
SELECT insert_new_album('Art collection', '01/01/2016', 1, 'Descripcion vacia', bytea_import('/usr/src/datosPoblar/caratulas/caratula.png'));
SELECT insert_new_album('Background music', '01/01/2018', 1, 'Descripcion vacia', bytea_import('/usr/src/datosPoblar/caratulas/caratula1.png'));
SELECT insert_new_album('My pop songs!', '01/01/2017', 2, 'Descripcion vacia', bytea_import('/usr/src/datosPoblar/caratulas/caratula2.png'));
SELECT insert_new_album('Scandinavian sound', '01/01/2017', 2, 'Descripcion vacia', bytea_import('/usr/src/datosPoblar/caratulas/caratula3.png'));
SELECT insert_new_album('In Aeternum', '01/01/2017', 3, 'Descripcion vacia', bytea_import('/usr/src/datosPoblar/caratulas/caratula4.png'));
SELECT insert_new_album('Belive in your success', '01/01/2015', 4, 'Descripcion vacia', bytea_import('/usr/src/datosPoblar/caratulas/caratula5.png'));
SELECT insert_new_album('Way to success', '01/01/2016', 4, 'Descripcion vacia', bytea_import('/usr/src/datosPoblar/caratulas/caratula6.png'));

-- canciones
SELECT insert_new_song('Uplifting Indie rock', bytea_import('/usr/src/datosPoblar/canciones/Uplifting_Indie_Rock.mp3'), 120, 1, 'rock');
SELECT insert_new_song('Country village', bytea_import('/usr/src/datosPoblar/canciones/Country_Village.mp3'), 63, 2, 'country');
SELECT insert_new_song('Jazz band', bytea_import('/usr/src/datosPoblar/canciones/Jazz_Band.mp3'), 126, 2, 'jazz');
SELECT insert_new_song('Slide guitar', bytea_import('/usr/src/datosPoblar/canciones/Slide_Guitar.mp3'), 207, 2, 'guitar');
SELECT insert_new_song('Hey sistah', bytea_import('/usr/src/datosPoblar/canciones/The_Moose_-_Hey_Sistah.mp3'), 180, 3, 'pop');
SELECT insert_new_song('One republic', bytea_import('/usr/src/datosPoblar/canciones/The_Moose_-_One_Republic.mp3'), 208, 3, 'pop');
SELECT insert_new_song('Lets get out', bytea_import('/usr/src/datosPoblar/canciones/The_Moose_-_Lets_Get_Out.mp3'), 194, 4, 'pop');
SELECT insert_new_song('Paramore vibe', bytea_import('/usr/src/datosPoblar/canciones/The_Moose_-_Paramore_Vibe.mp3'), 183, 4, 'pop');
SELECT insert_new_song('We got the love', bytea_import('/usr/src/datosPoblar/canciones/The_Moose_-_We_Got_The_Love.mp3'), 154, 4, 'pop');
SELECT insert_new_song('I love her', bytea_import('/usr/src/datosPoblar/canciones/I_Love_Her.mp3'), 218, 5, ' electronic');
SELECT insert_new_song('Minimal perception', bytea_import('/usr/src/datosPoblar/canciones/Minimal_Perception.mp3'), 252, 5, 'techno');
SELECT insert_new_song('Belive in your success', bytea_import('/usr/src/datosPoblar/canciones/Believe_in_your_success.mp3'), 247, 6, 'rock');
SELECT insert_new_song('Way to success', bytea_import('/usr/src/datosPoblar/canciones/Way_to_Success.mp3'), 186, 7, 'piano');
SELECT insert_new_song('Success', bytea_import('/usr/src/datosPoblar/canciones/Success.mp3'), 212, 6, 'pop');

--mix
SELECT insert_song_in_list(1,8);
SELECT insert_song_in_list(1,9);
SELECT insert_song_in_list(1,10);

SELECT follow_user(1, 4);
SELECT follow_user(1, 2);
SELECT follow_user(2, 1);
