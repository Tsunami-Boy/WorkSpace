USE BD_Usm_Spot

IF OBJECT_ID('repositorio_musica') IS NULL
BEGIN
	CREATE TABLE repositorio_musica(
		id INTEGER PRIMARY KEY IDENTITY(1,1),
		position INTEGER NOT NULL,
		artist_name VARCHAR(100) NOT NULL,
		song_name VARCHAR(100) NOT NULL,
		days INTEGER NOT NULL,
		top_10 INTEGER NOT NULL,
		peak_position INTEGER NOT NULL,
		peak_position_time VARCHAR(100) NOT NULL,
		peak_streams INTEGER NOT NULL,
		total_streams INTEGER NOT NULL
	);
END


IF OBJECT_ID('reproduccion') IS NULL
BEGIN
	CREATE TABLE reproduccion(
		id INTEGER PRIMARY KEY,
		song_name VARCHAR(100) NOT NULL,
		artist_name VARCHAR(100) NOT NULL,
		fecha_reproduccion DATE NOT NULL,
		cant_reproducciones INTEGER NOT NULL,
		favorito BIT DEFAULT 0,
	);
END

IF OBJECT_ID('lista_favoritos') IS NULL
BEGIN
CREATE TABLE lista_favoritos(
	id INTEGER PRIMARY KEY,
	song_name VARCHAR(100) NOT NULL,
	artist_name VARCHAR(100) NOT NULL,
	fecha_agregada DATE NOT NULL,
);
END