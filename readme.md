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
dokku apps:create col
```

2. On client:

```sh
git remote add dokku dokku@<IPADDRESS>:col

```

3. On server:

```sh
# create a persistant directory
dokku storage:ensure-directory col
dokku storage:mount col /var/lib/dokku/data/storage/col:/app/storage

# set up settings
dokku config:set --no-restart col DB_URL=**DATABASE URL**
dokku config:set --no-restart col GOOGLE_ANALYTICS=********
dokku config:set --no-restart col PROMETHEUS_AUTH_PASSWORD=********
dokku config:set --no-restart col DATA_DIR=/app/storage/data
dokku config:set --no-restart col FLASK_APP=coltracker.app:server

# set up redis
dokku redis:create coltrackercache
dokku redis:link coltrackercache col

# fetch data
dokku run col flask fetch-data
dokku run col flask clear-cache
dokku ps:rebuild col
```

4. Set up cron tab for scheduled tasks (on server)

```sh
nano /etc/cron.d/col
```
