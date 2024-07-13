import sqlite3

conn = sqlite3.connect('youtube_video.db')

cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL 
    )
''')


def list_all_videos():
    cur.execute("SELECT * FROM videos") #hold the result
    for row in cur.fetchall():
        print(row)

def add_video(name, time):
    cur.execute("INSERT INTO videos(name,time) VALUES (?, ?)", (name,time))
    conn.commit()

def update_video(video_id,name,time):
    cur.execute("UPDATE videos set name = ?, time = ? WHERE id = ?", (name,time,video_id))
    conn.commit()

def delete_video(video_id):
    cur.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()


def main():
    while True:

        print("\n youtube Manager | choose an option")
        print("1. List all favorite videos")
        print("2. Add a Youtube Video")
        print("3. Update a Youtube Video Details")
        print("4. Delete a Youtube Video")
        print("5. Exit... the app")

        choice = input("Enter your choice: ")
        # print(videos)

        if choice == '1':
            list_all_videos()

        elif choice == '2':
            name = input("Enter the video name : ")
            time = input("Enter the video time : ")
            add_video(name,time)

        elif choice == '3':
            video_id = input("Enter a video ID to update : ")
            name = input("Enter the video name : ")
            time = input("Enter the video time : ")
            update_video(video_id, name, time)

        elif choice == '4':
            video_id = input("Enter a video ID to delete : ")
            delete_video(video_id)

        elif choice == '5':
            break

        else:
            print("Invalid choice")

    conn.close()


if __name__ == "__main__":
    main()