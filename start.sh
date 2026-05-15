#!/bin/bash

echo "🧹 Cleaning old containers..."
docker compose down --remove-orphans -v

echo "🧼 Removing unused networks..."
docker network prune -f

echo "💾 Removing dangling volumes (optional safe reset)..."
docker volume prune -f

echo "🚀 Rebuilding full system..."
docker compose up --build