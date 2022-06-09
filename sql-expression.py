from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from our localhost "chinook" db
db = create_engine("postgresgl:///chinook")

meta = MetaData(db)

# create variable for "Artist" table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# create variable for "Album" table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# create table for "Track" table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# making the connection
with db.connect() as connection:

    # Query 1 - select all records from the "Artist" table
    #select_query = artist_table.select()

    # Query 2 - select only the "Name" column from the "Artist" table
    #select_query = artist_table.select().with_only_columns([artist_table.c.Name])

    # Query 3 - select only the 'Queen' column from the "Artist" table
    #select_query = artist_table.select().where(artist_table.c.Name == 'Queen')

    # Query 4 - select only the 'AristId' #51 from the "Artist" table
    #select_query = artist_table().where(artist_table.c.ArtistId == 51)

    # Query 5 - select only the albums with the 'AristId' #51 on the "Artist" table
    #select_query = album_table().where(artist_table.c.ArtistId == 51)

    results = connection.execute(select_query)
    for result in results:
        print(result)