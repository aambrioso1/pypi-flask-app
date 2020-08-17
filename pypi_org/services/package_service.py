import os
import sys
from typing import List, Optional
import sqlalchemy.orm

# Make it run more easily outside of PyCharm
sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..")))

import pypi_org.data.db_session as db_session
from pypi_org.data.package import Package
from pypi_org.data.releases import Release


def get_latest_releases(limit = 10) -> List[Release]:
	session = db_session.create_session()

	releases = session.query(Release). \
		options(sqlalchemy.orm.joinedload(Release.package)). \
		order_by(Release.created_date.desc()). \
		limit(limit). \
		all()
	session.close()
	return releases

# Returns package count for webpage output
def get_package_count() -> int:
	session = db_session.create_session()
	return session.query(Package).count() # query here accesses the data base

# Returns release count for webpage output
def get_release_count() -> int:
	session = db_session.create_session()
	return session.query(Release).count() # query here accesses the data base


def get_package_by_id(package_id: str) -> Optional[Package]:
	if not package_id:
		return None

	package_id = package_id.strip().lower()
	
	session = db_session.create_session()


	package = session.query(Package) \
		.options(sqlalchemy.orm.joinedload(Package.releases)) \
		.filter(Package.id == package_id) \
		.first()
		# What is the above code doing?

	session.close()
	
	return package