import pytest

from application import create_app, db
from application.models import Tip, Tag

@pytest.fixture(scope='session')
def app():
    app = create_app('testing')
    app_context = app.app_context()
    app_context.push()
    with app.app_context():
        db.create_all()
        db.session.add(Tip("First!", "Here should be url"))
        db.session.add(Tip("Another tip", "Imagine url here too"))
        db.session.commit()
    
    yield app

    db.session.remove()
    db.drop_all()
    app_context.pop()

def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')