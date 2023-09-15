# Rss-feed
## Project Description

This project aims to develop an RSS feed aggregator using Django. The aggregator will extract and store data from various RSS feed sources, including APIs and custom XML feeds. It will implement advanced parsing techniques, data mapping, and flexible schema design to accommodate diverse feed structures. The project will also include custom JWT authentication using Redis to store access tokens and utilize and PostgreSQL as the database.

Follow these steps to set up the project locally:

1. Clone the repository:

   ```bash
   git clone https://github.com/Mohammad-R-N/Rss-feed.git
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run migrations to create the database schema:

   ```bash
   python manage.py migrate
   ```

6. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

The project should now be running locally at `http://localhost:8000/`.


## Running the Parsing Process

To parse the podcast feeds and populate your database with podcast episodes, you can use the following management command:

```bash
python manage.py parse_podcast
```

This command will trigger the parsing process, fetching the RSS feeds you added through the Django admin panel and updating your database with podcast episode data.


## Usage

To use these endpoints, you can make GET and POST requests to the URLs listed above as per your requirements. For example:

- To list all podcasts, make a GET request to `/podcasts/`.
- To retrieve details of a specific podcast with ID 1, make a GET request to `/podcasts/1/`.
- To list episodes of a specific podcast with ID 1, make a GET request to `/podcasts/1/episodes/`.
- To retrieve details of a specific episode with ID 1, make a GET request to `/episodes/1/`.-