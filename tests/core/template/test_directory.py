import os
from pathlib import Path
from typing import Dict, List

import pytest

from web_ninja.core.template.directory import DirectoryTemplate


class FakeDirectoryTemplate(DirectoryTemplate[Dict[str, Path]]):
    def render(self, context: Dict[str, Path]) -> None:
        self.child_dirs = [self.path / child_dir for child_dir in context["child_dirs"]]
        self.child_files = [
            self.path / child_file for child_file in context["child_files"]
        ]


@pytest.fixture
def temp_dirs():
    temp_dirs = [Path(f"temp_dir{i}") for i in range(3)]
    yield temp_dirs
    for temp_dir in temp_dirs:
        os.rmdir(Path("/tmp") / temp_dir)


@pytest.fixture
def temp_files():
    temp_files = [Path(f"temp_file{i}") for i in range(3)]
    yield temp_files
    for temp_file in temp_files:
        os.remove(Path("/tmp") / temp_file)


def test_directory_template(temp_dirs: List[Path], temp_files: List[Path]):
    path = Path("/tmp")
    template = FakeDirectoryTemplate(path=path)
    context = {
        "child_dirs": temp_dirs,
        "child_files": temp_files,
    }
    template.render(context)
    template.generate()

    assert all([child_dir.exists() for child_dir in template.child_dirs])
    assert all([child_file.exists() for child_file in template.child_files])
    assert all([child_dir.is_dir() for child_dir in template.child_dirs])
    assert all([child_file.is_file() for child_file in template.child_files])
