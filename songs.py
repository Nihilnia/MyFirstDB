import sqlite3, random

connect = sqlite3.connect("mySongList.db")
cursor = connect.cursor()

# Creating Function for Create A Table ON DATABASE

def createTable():

    cursor.execute("CREATE TABLE IF NOT EXISTS mySongs (SongName TEXT, Artist Text, SongID INT)")
    connect.commit()

createTable()

if createTable:
    message = "Database is created!"
    print("\n\n", "# " * (int(len(message) / 2 + 4)), sep = "")
    print("# ", message, "  #")
    print("# " * (int(len(message) / 2 + 4)), "\n\n")
else:
    print("Somethings gone wrong!")


# Creating A Function For Add A New Song

def addSong(songName = "Uknown", artist = "Unknown", songID = 0000):

    songName = input("Song name: ")
    artist = input("Artist: ")
    songID = random.randint(0000, 9999)

    cursor.execute("Insert into mySongs Values(?, ?, ?)", (songName, artist, songID))
    connect.commit()


# Creating A Function For Update The Song List

def updateTheTable():

    userUpdateChoice = input("""
    What do you want to update?

    1) Update an artist name

    2) Update a song name

    3) Cancel
    """)

    if userUpdateChoice == "1":
        oldArtistName = input("Which artist: ")
        newArtistName = input("New Artist: ")

        cursor.execute("Update mySongs set Artist = (?) where Artist = (?)", (newArtistName, oldArtistName, ))
        connect.commit()

        print("Updated succesfuly!")

    elif userUpdateChoice == "2":
        oldSongName = input("Which song: ")
        newSongName = input("New song name: ")

        cursor.execute("Update mySongs set songName = (?) where songName = (?)", (newSongName, oldSongName))
        connect.commit()

#Creating A Function For Delete Anything From The List

def deleteAnything():

    userDeleteChoice = input("""
    What do you want to delete

    1) Delete A Song

    2) Delete all Songs of An Artist

    3) Cancel
    """)

    if userDeleteChoice == "1":
        deleteSong = input("Which song you wanna delete?: ")

        cursor.execute("Delete from mySongs where songName = (?)", (deleteSong, ))
        connect.commit()

        print("Song Deleted!")
    
    elif userDeleteChoice == "2":
        deleteArtist = input("Which artist do you wanna delete?: ")
        cursor.execute("Delete from mySongs where artist = (?)", (deleteArtist, ))
        connect.commit()

        print("Artist Deleted!")


# Creating A Function For See The All Songs/Infos

def seeAllSongs():
    cursor.execute("Select * from mySongs")
    allSongs = cursor.fetchall()

    print("""
        - - - - ALL SONGS - - - -""")

    for f in allSongs:
        print("""        
        Artist:     {}
        Song Name:  {}
        Song ID:    {}
        """.format(f[0], f[1], f[2]))


# Creating A Function For See Spesific Artist's Songs

def seeAsArtist(artistName):
    cursor.execute("Select songName, songID from mySongs where artist = (?)", (artistName, ))
    songsOfArtist = cursor.fetchall()

    print("""
        - - - - All songs of {} - - - -""".format(artistName))

    for f in songsOfArtist:
        print("""
        Song Name:  {}
        Song ID:    {}

        """.format(f[0], f[1]))

print("Welcome to add & search tool of your DataBase!")

while True:
    userChoice = input("""

    ---- M A I N  M E N U ----

    1) Add New song
    
    2) See all songs

    3) Search a spesific artist's songs

    4) Update options

    5) Delete Options

    6) Exit

    """)
    if userChoice == "1":
        addSong()
        if addSong:
            print("")
            print("*" * 30)
            print("Informations of songs added to databese.")
            print("*" * 30, "\n\n")
        else:
            print("Somethings gone wrong!")
    
    elif userChoice == "2":
        seeAllSongs()
    
    elif userChoice == "3":
        userArtist = input("Artist name: ")
        seeAsArtist(userArtist)

    elif userChoice == "4":
        updateTheTable()

    elif userChoice == "5":
        deleteAnything()

    else:
        print("See ya next time!")
        break

connect.close()