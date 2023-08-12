import os
import psycopg2

def index_videos(directory_path, conn):
    cursor = conn.cursor()
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(('.mp4', '.avi')): # Adjust extensions as needed
                file_path = os.path.join(root, file)
                video_id = os.path.splitext(file)[0] # Determine ID as needed
                size = os.path.getsize(file_path)
                length = None # Get length using a library like moviepy if needed
                
                # Insert into the database
                cursor.execute(
                    "INSERT INTO video_index (video_id, size, length, source_path) VALUES (%s, %s, %s, %s)",
                    (video_id, size, length, file_path)
                )
    
    conn.commit()
    cursor.close()

# Database connection parameters
conn_params = {
    'dbname': 'your_dbname',
    'user': 'your_user',
    'password': 'your_password',
    'host': 'your_host',
    'port': 'your_port'
}

# Directory where videos are stored on NAS
directory_path = "/path/to/videos"

# Connect to the database
conn = psycopg2.connect(**conn_params)

# Index the videos
index_videos(directory_path, conn)

# Close the connection
conn.close()