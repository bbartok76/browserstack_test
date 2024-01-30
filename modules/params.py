import pytest
from modules.context import ctx


invalid_email_params = pytest.mark.parametrize(
    "email, password", ctx["credentials"]["credentials"].get("invalid", [])
)
valid_email_params = pytest.mark.parametrize(
    "email, password", ctx["credentials"]["credentials"].get("valid", [])
)
