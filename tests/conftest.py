import pytest
from project import create_app
from flask import current_app
from project.models import Stock
from project import database

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()
    flask_app.config.from_object('config.TestingConfig')

    # Creating test client
    with flask_app.test_client() as testing_client:
        # Establishing the application context for logging 
        with flask_app.app_context():
            current_app.logger.info('In the test_client() fixture...')

            # Create the database and the database table(s)
            database.create_all()

        yield testing_client  # this is where the testing happens!

        with flask_app.app_context():
            database.drop_all()



@pytest.fixture(scope='module')
def new_stock():
    stock = Stock('BTC', '10', '15000')
    return stock