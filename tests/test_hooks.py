import pytest
from cookiecutter.main import cookiecutter
from cookiecutter.exceptions import FailedHookException


def test_wrong_config1(tmpdir):
    """ Test that numbers are not allowed in the project name."""
    with pytest.raises(FailedHookException):
        cookiecutter(
            template=".",
            config_file="tests/wrong_config1.yaml",
            overwrite_if_exists=True,
            no_input=True,
            output_dir=str(tmpdir),
        )
        

def test_wrong_config2(tmpdir):
    """ Test that numbers are not allowed in the project name."""
    with pytest.raises(FailedHookException):
        cookiecutter(
            template=".",
            config_file="tests/wrong_config2.yaml",
            overwrite_if_exists=True,
            no_input=True,
            output_dir=str(tmpdir),
        )


def test_wrong_config3(tmpdir):
    """ Test that numbers are not allowed in the project name."""
    with pytest.raises(FailedHookException):
        cookiecutter(
            template=".",
            config_file="tests/wrong_config3.yaml",
            overwrite_if_exists=True,
            no_input=True,
            output_dir=str(tmpdir),
        )
