# coding: utf-8

import pytest
from rest_framework.test import APIClient
from pytest_django.django_compat import is_django_unittest


@pytest.fixture(autouse=True)
def monkeypatch_search_path(monkeypatch):
    import os
    import sys

    ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, ROOT_PATH)
    sys.path.insert(0, os.path.join(ROOT_PATH, 'apps'))


@pytest.fixture(scope='session')
def api_client():
    api_client = APIClient()
    return api_client


@pytest.fixture(autouse=True)
def monkeypatch_rest_framework_settings(monkeypatch):
    from django.conf import settings

    REST_FRAMEWORK = settings.REST_FRAMEWORK
    REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES'] = ()
    REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] = ()
    monkeypatch.setattr(settings, 'REST_FRAMEWORK', REST_FRAMEWORK)


@pytest.fixture(scope='session')
def django_db_setup():
    # override this fixture to use the existing db
    pass


@pytest.fixture(scope='function')
def db(request, django_db_setup, django_db_blocker):
    """
    Override this fixture from pytest-django to support multi db
    """
    from django.test import TestCase    # NOQA

    class MultiDBTestCase(TestCase):
        multi_db = True

        def _fixture_setup(self):
            assert not self.reset_sequences, 'reset_sequences cannot be used on TestCase instances'
            self.atomics = self._enter_atomics()

        def _fixture_teardown(self):
                self._rollback_atomics(self.atomics)

    if is_django_unittest(request):
        return

    django_db_blocker.unblock()
    test_case = MultiDBTestCase(methodName='__init__')
    test_case._pre_setup()
    request.addfinalizer(test_case._post_teardown)
