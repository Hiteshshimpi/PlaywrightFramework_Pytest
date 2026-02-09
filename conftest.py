import pytest


@pytest.fixture(scope='session')
#request is used to return the parameter associated wth that testcase
def usercred(request):
    return request.param