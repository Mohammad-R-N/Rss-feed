# Rss-feed
RSS Feed Aggregator Project

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