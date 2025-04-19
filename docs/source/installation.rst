Installation
============

Prerequisites
-------------

- Python 3.8+
- MySQL server
- Kivy framework

Setup Steps
-----------

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/Sam-Gaudet/DatabasesAss4.git
      cd tasklist-app

2. Create a virtual environment:

   .. code-block:: bash

      python -m venv venv
      source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies:

   .. code-block:: bash

      pip install -r requirements.txt

4. Set up the database:

   .. code-block:: bash

      mysql -u root -p < db_creation.sql

5. Configure environment variables:

   Copy the `.env.example` to `.env` and update the database credentials.