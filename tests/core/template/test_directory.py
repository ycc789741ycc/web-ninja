import os
from pathlib import Path
from typing import Dict, List

import pytest

from web_ninja.core.template.directory import DirectoryTemplate


class FakeDirectoryTemplate(DirectoryTemplate[Dict[str, Path]]):
    def __init__(
        self, base_dir: Path, child_dirs: List[Path], child_file_paths: List[Path]
    ) -> None:
        super().__init__(base_dir)
        self.child_dirs = [self.base_dir / child_dir for child_dir in child_dirs]
        self.child_file_paths = [
            self.base_dir / child_file_path for child_file_path in child_file_paths
        ]

    def render(self, context: Dict[str, Path]) -> None:
        pass


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
    template = FakeDirectoryTemplate(
        base_dir=path, child_dirs=temp_dirs, child_file_paths=temp_files
    )
    template.generate()

    assert all([child_dir.exists() for child_dir in template.child_dirs])
    assert all(
        [child_file_path.exists() for child_file_path in template.child_file_paths]
    )
    assert all([child_dir.is_dir() for child_dir in template.child_dirs])
    assert all(
        [child_file_path.is_file() for child_file_path in template.child_file_paths]
    )
