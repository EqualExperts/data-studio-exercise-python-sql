## Exercise Instructions

This is a bootstrap project to load interesting data from a Stack Exchange dataset into a data warehouse.
You are free to change anything about this bootstrap solution as you see fit, so long as it can still be executed by a reviewer.

- The project is set up to use Pipenv & Python 3.8
- SQLite3 provides an infrastructure-free simple data warehouse stand-in
- Facilites for linting etc. are provided as scripts and integrated with Pipenv

[scripts/fetch_data.sh](scripts/fetch_data.sh) is provided to download and decompress the dataset.

Your task is to make the Posts and Tags content available in an SQLite3 database.
[src/main.py](src/main.py) is provided as an entrypoint, and has an example of parsing the source data.
[src/db.py](src/db.py) is empty, but the associated test demonstrates interaction with an SQLite3 database.
You should ensure your code is correctly formatted and lints cleanly.

You will aim to make it convenient for data scientists to execute analytics-style queries reliably over the Posts and Tags tables.
You will be asked to demonstrate the solution, including:
- how you met the data scientist needs
- how you did (or would) ensure data quality
- what would need to change for the solution scale to work with a 10TB dataset with new data arriving each day

## Your Writeup!

Please include any instructions, answers and details of any import decisions you made here for the reviewer.
