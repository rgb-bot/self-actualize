#!/bin/bash
export PYTHONPATH=$PYTHONPATH:/sendMessage


# Step 1: Start the Docker container using docker-compose
echo "Starting PostgreSQL container..."
docker-compose up -d

# Step 2: Wait for PostgreSQL to be ready
echo "Waiting for PostgreSQL to start..."
sleep 10  # Adjust based on your container's startup time

# Step 3: Run the table creation script inside the container
echo "Running the table creation script..."
docker exec -i $(docker ps -q -f "name=db") psql -U user -d messages < ./init.sql

echo "Database setup complete!"