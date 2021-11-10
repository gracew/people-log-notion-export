# People Log Notion Export

This project contains a simple script to export data from Notion in CSV format.

To run:
```
NOTION_API_KEY=<integration token> pipenv run python to_csv.py
```

This should produce 2 files, `people.csv` and `log.csv`, that can then be imported into Postgres.

First, initialize the database:
```
PGPASSWORD=<pg password> psql -h <pg host> -U <pg username> <pg database name> < ./create_tables.sql
```

Then within the psql prompt:
```
\copy people(id, name, context, how_i_know_them) from '<path to people.csv>' delimiter ',' csv;
\copy log(date, hours, type, person_id) from '<path to log.csv>' delimiter ',' csv;
```
