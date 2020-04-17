import json
import os
import datetime

from sqlalchemy import create_engine
import click

from settings import DB_URL, GRANTS_DATA_FILE, FUNDER_IDS_FILE

@click.command()
@click.option('--db-url', default=DB_URL, help='Database connection string')
@click.option('--grants-data-file', default=GRANTS_DATA_FILE, help='Location to save the grants data')
@click.option('--funder-ids-file', default=FUNDER_IDS_FILE, help='Location to save the list of funders')
def fetch_data(db_url=DB_URL, grants_data_file=GRANTS_DATA_FILE, funder_ids_file=FUNDER_IDS_FILE):
    """Import data from the database to a JSON file"""
    engine = create_engine(db_url)
    conn = engine.connect()

    grant_sql = '''
    select g.data
    from view_latest_grant g
    where (
            g.data->>'title' ~* 'covid|coronavirus|pandemic' or
            g.data->>'description' ~* 'covid|coronavirus|pandemic' or
            g.data->'grantProgramme'->0->>'title' ~* 'covid|coronavirus|pandemic'
        )
        and to_date(g.data->>'awardDate', 'YYYY-MM-DD') > '2020-03-16'
    order by to_date(g.data->>'awardDate', 'YYYY-MM-DD'), g.data->>'id'
    '''

    print('Fetching grants')
    result = conn.execute(grant_sql)

    grants = []
    for row in result:
        grants.append(row['data'])
    print('Found {:,.0f} grants'.format(len(grants)))

    print('Saving to file')
    with open(grants_data_file, 'w') as a:
        json.dump({
            "grants": grants,
            "last_updated": datetime.datetime.now().isoformat()
        }, a, indent=4)
    print('Saved to `{}`'.format(grants_data_file))

    print('Fetching funders')
    result = conn.execute('''
    select distinct g.data->'fundingOrganization'->0->>'id' as "fundingOrganization.0.id"
    from view_latest_grant g 
    ''')
    funders = []
    with open(funder_ids_file, 'r') as a:
        funders.extend(json.load(a).get('funders', []))
    for row in result:
        funders.append(row['fundingOrganization.0.id'])
    funders = sorted(set(funders))
    print('Found {:,.0f} funder IDs'.format(len(funders)))

    print('Saving to file')
    with open(funder_ids_file, 'w') as a:
        json.dump({
            "funders": funders,
        }, a, indent=4)
    print('Saved to `{}`'.format(funder_ids_file))

if __name__ == '__main__':
    fetch_data()