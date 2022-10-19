# 360Giving Cost of Living Grants Tracker

![360Giving Logo](https://www.threesixtygiving.org/wp-content/themes/360giving2020/assets/images/360-logos/360giving-main.svg)

A tracker for UK grants published to the [360Giving Data Standard](http://standard.threesixtygiving.org/),
using data from the [360Giving Datastore](https://www.threesixtygiving.org/data/360giving-datastore/).

The app is built using [Dash by Plotly](https://dash.plotly.com/), which is based around the Flask
python web framework and react.

## Run development version

```sh
python -m venv env # create virtual env
source env/bin/activate # enter virtual environment (`env/Scripts/activate` on windows)
pip install -r requirements.txt # install needed requirements
mv .env-sample .env # rename .env file (linux)
```

You'll then need to edit the `.env` file, adding the correct values for `DB_URL` (the database connection
for the 306Giving Datastore) and `MAPBOX_TOKEN` (which shows the map).

Once the settings are correct you need to fetch the latest data.

```sh
flask fetch-data
```

Finally run the development server

```sh
python index.py
```

## Setup using [dokku](http://dokku.viewdocs.io/dokku/)

1. On server:

```sh
dokku apps:create coltracker
```

2. On client:

```sh
git remote add dokku dokku@<IPADDRESS>:coltracker

```

3. On server:

```sh
# create a persistant directory
mkdir -p  /var/lib/dokku/data/storage/coltracker
chown -R dokku:dokku /var/lib/dokku/data/storage/coltracker
chown -R 32767:32767 /var/lib/dokku/data/storage/coltracker
dokku storage:mount coltracker /var/lib/dokku/data/storage/coltracker:/app/storage

# set up settings
dokku config:set coltracker DB_URI=**DATABASE URL**
dokku config:set coltracker GOOGLE_ANALYTICS=********
dokku config:set coltracker PROMETHEUS_AUTH_PASSWORD=********
dokku config:set -no-restart coltracker DATA_DIR=/app/storage/data
dokku config:set -no-restart coltracker FLASK_APP=coltracker.app:server

# set up redis
dokku redis:create coltrackercache
dokku redis:link coltrackercache coltracker

# fetch data
dokku run coltracker flask fetch-data
dokku run coltracker flask clear-cache
dokku ps:rebuild coltracker
```

4. Set up cron tab for scheduled tasks (on server)

```sh
nano /etc/cron.d/coltracker
```
