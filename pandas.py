import sqlite3

# Connect to an SQLite database (create it if it doesn't exist)
conn = sqlite3.connect('db.sqlite3')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Execute SQL commands
cursor.execute('CREATE TABLE IF NOT EXISTS sub (id INTEGER PRIMARY KEY, name TEXT)')

# Insert data into the database
cursor.execute('INSERT INTO users (name) VALUES (?)', ('John',))

# Commit the changes
conn.commit()

# Retrieve data from the database
cursor.execute('SELECT * FROM users')
data = cursor.fetchall()

# Print the data
for row in data:
    print(row)

# Close the cursor and the connection
cursor.close()
conn.close()
