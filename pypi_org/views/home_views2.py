import os
import sys
import flask

# Make it run more easily outside of PyCharm
sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..")))

from pypi_org.infrastructure.view_modifiers import response
import pypi_org.services.package_service as package_service
import pypi_org.services.user_service as user_service
from pypi_org.infrastructure import cookie_auth

blueprint = flask.Blueprint('home', __name__, template_folder='templates')

@blueprint.route('/')
@response(template_file='home/index.html')

# Sets up the index page
def index():
	return {
		'releases':  package_service.get_latest_releases(), # gets the list of packages
		'package_count': package_service.get_package_count(), # gets the package count
		'release_count': package_service.get_release_count(), # gets the release count
		'user_count': user_service.get_user_count(), # gets the user count
		'user_id': cookie_auth.get_user_id_via_auth_cookie(flask.request),
	}
	# return flask.render_template('home/index.html', packages=test_packages)

@blueprint.route('/about')
@response(template_file='home/about.html')
def about():
	return {
		'user_id': cookie_auth.get_user_id_via_auth_cookie(flask.request),
	}
	# return flask.render_template('home/about.html')