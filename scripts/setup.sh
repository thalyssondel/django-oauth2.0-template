#!/bin/bash

# Ensure the script runs from the project root
cd "$(dirname "$0")/.."

# Terminal Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[1;34m'
NC='\033[0m' # No Color

# 1. System OS Verification
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    echo -e "${RED}⚠️  ERROR: Bash script detected on native Windows environment.${NC}"
    echo "Please use the PowerShell equivalent: .\scripts\windows\setup.ps1"
    exit 1
fi

# 2. Performance Optimization for WSL/Cross-FS
# Prevents hardlink errors when working across Windows/Linux filesystems
export UV_LINK_MODE=copy

echo -e "${YELLOW}🛡️  Starting Setup${NC}"c

# 3. Dependency Management (UV vs. Traditional Venv)
if command -v uv &> /dev/null; then
    echo -e "⚡ ${GREEN}UV detected!${NC} Synchronizing project..."
    uv sync
    source .venv/bin/activate
else
    echo -e "📦 UV not found. Proceeding with ${YELLOW}standard venv${NC}..."
    python3 -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
    pip install -e .
fi

# 4. Infrastructure Setup (Docker)
echo "🐳 Starting database containers..."
docker-compose up -d

# Wait for PostgreSQL to be fully ready for connections
echo -n "⏳ Waiting for database to be ready..."
until docker-compose exec db pg_isready -U $(grep DB_USER .env | cut -d '=' -f2) > /dev/null 2>&1; do
  echo -n "."
  sleep 1
done
echo -e "\n✅ Database is up and running."

# 5. Database Migrations
echo "🗄️  Running database migrations..."
python manage.py migrate

# 6. Administrator Interaction Block
echo ""
echo -e "${BLUE}----------------------------------------------------------${NC}"
echo -e "${GREEN}👤 ADMINISTRATOR SETUP (SUPERUSER)${NC}"
echo -e "Create your account to access the admin panel."
echo -e "${BLUE}----------------------------------------------------------${NC}"
echo ""

python manage.py createsuperuser

# 7. Finalization
echo -e "${BLUE}----------------------------------------------------------${NC}"
echo -e "${GREEN}✨ Setup completed successfully!${NC}"
echo -e "To start working, activate your environment and run the server:"
echo ""
echo -e "   ${YELLOW}source .venv/bin/activate${NC}"
echo -e "   ${YELLOW}python manage.py runserver${NC}"
echo -e "${BLUE}----------------------------------------------------------${NC}"