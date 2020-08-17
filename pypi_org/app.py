  
import os
import sys
import flask

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

import pypi_org.data.db_session as db_session

"""
from infrastructure.view_modifiers import response
import services.package_service as ps
"""
app = flask.Flask(__name__)

def main():
	register_blueprints()
	setup_db()
	app.run(debug=True)

def setup_db():
	db_file = os.path.join(
		os.path.dirname(__file__),
		'db',
		'pypi.sqlite')

	db_session.global_init(db_file)

def register_blueprints():
    from pypi_org.views import home_views
    from pypi_org.views import package_views
    from pypi_org.views import cms_views
    from pypi_org.views import account_views

    app.register_blueprint(package_views.blueprint)
    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(account_views.blueprint)
    app.register_blueprint(cms_views.blueprint)

"""
@app.route('/')
@response(template_file='home/index.html')
def index():
	test_packages = ps.get_latest_packages()
	return {'packages':  test_packages}
	# return flask.render_template('home/index.html', packages=test_packages)

@app.route('/about')
@response(template_file='home/about.html')
def about():
	return {}
	# return flask.render_template('home/about.html')
"""

if __name__ == '__main__':
	main()
else:
	configure()