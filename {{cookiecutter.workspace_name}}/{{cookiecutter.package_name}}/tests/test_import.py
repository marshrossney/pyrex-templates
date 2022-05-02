import pytest

def test_import_package():
    import {{cookiecutter.package_name}}


def test_import_missing_module():
    with pytest.raises(ImportError):
        import numpy
