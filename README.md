# Shortyurl

## Setup instructions
0. You need to have pre-installed executables of `docker` and `docker-compose` 
1. `docker-compose build`
2. `docker-compose up -d`
3. `docker-compose exec django ./manage.py migrate`

## Other commands
- `docker-compose exec django pytest` - runs unittests

## Usage
- POST `http://127.0.0.1:8000/api/v1/urls/` `{"original_url": "https://www.tier.app/"}` - creates short version of a URL
- GET `http://127.0.0.1:8000/api/v1/urls/<alias>` - gets URL by its alias (and also counts a "visit")