# to stop on first error
set -e


export FLASK_APP=api.server

echo "Running migrations started ... (@timestamp : $(date +%s); @datetime : $(date "+%Y-%m-%d %H:%M:%S") ($(date +"%r"))"

python -m alembic.config --config=core/migrations/alembic.ini upgrade head

echo "Running migrations ended ... (@timestamp : $(date +%s); @datetime : $(date "+%Y-%m-%d %H:%M:%S") ($(date +"%r"))"


flask run -p 8421 --host=0.0.0.0