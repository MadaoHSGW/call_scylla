from cassandra.cluster import Cluster

# Connect to ScyllaDB
cluster = Cluster(['192.168.10.74'])  # Replace with the IP address or hostname of your ScyllaDB container
session = cluster.connect()

# Create a keyspace and use it
session.execute("CREATE KEYSPACE IF NOT EXISTS my_keyspace WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1}")
session.execute("USE my_keyspace")

# Create a table
session.execute("""
    CREATE TABLE IF NOT EXISTS my_table (
        id UUID PRIMARY KEY,
        data text
    )
""")

# Insert data into the table
prepared_insert = session.prepare("INSERT INTO my_table (id, data) VALUES (?, ?)")

# Replace with your data
data_to_insert = (uuid.uuid4(), "Hello, ScyllaDB!")

session.execute(prepared_insert, data_to_insert)

# Close the session and cluster when done
session.shutdown()
cluster.shutdown()
