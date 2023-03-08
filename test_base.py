import pytest


# Default fixture to pass urls to other modules
@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass
