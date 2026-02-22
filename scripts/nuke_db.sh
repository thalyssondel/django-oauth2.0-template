#!/bin/bash

# Ensure the script runs from the project root (assuming it's in scripts/linux/)
cd "$(dirname "$0")/.."

# Terminal Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${RED}☢️  WARNING: This will permanently delete all database containers and DATA!${NC}"
read -p "Are you sure you want to proceed? (y/N): " confirm

if [[ $confirm == [yY] ]]; then
    echo -e "${YELLOW}💣 Stopping infrastructure and removing persistent volumes...${NC}"
    
    # -v flag removes named volumes declared in the 'volumes' section of the compose file
    docker-compose down -v
    
    echo -e "\n${GREEN}✨ System cleared successfully.${NC}"
else
    echo -e "${YELLOW}Operation cancelled.${NC} No changes were made."
fi