import os
from pathlib import Path
from typing import List

import pytest

from web_ninja.core.template.module import ModuleFile, ModuleTemplate


class FakeModuleTemplate(ModuleTemplate):
    def __init__(self, base_dir: Path, child_dirs: List[Path], module_files: List[ModuleFile]) -> None:
        super().__init__(base_dir)
        self.child_dirs = child_dirs
        self.module_files = module_files


@pytest.fixture
def temp_dirs():
    temp_dirs = [Path("temp_dir1"), Path("temp_dir2")]
    yield temp_dirs
    for temp_dir in temp_dirs:
        os.rmdir(Path("/tmp") / temp_dir)


@pytest.fixture
def temp_module_files():
    temp_module_files = [
        ModuleFile(Path("temp_dir1/temp_file1"), "content1 {{ name_1 }}"),
        ModuleFile(Path("temp_dir2/temp_file2"), "content2 {{ name_2 }}"),
    ]
    yield temp_module_files
    for temp_module_file in temp_module_files:
        os.remove(Path("/tmp") / temp_module_file.child_path)


def test_directory_template(temp_dirs: List[Path], temp_module_files: List[ModuleFile]):
    path = Path("/tmp")
    template = FakeModuleTemplate(path, temp_dirs, temp_module_files)
    context = {"name_1": "test_name_1", "name_2": "test_name_2"}
    template.render(context)
    template.generate()

    with open(path / temp_module_files[0].child_path, "r") as file:
        assert file.read() == "content1 test_name_1"
    with open(path / temp_module_files[1].child_path, "r") as file:
        assert file.read() == "content2 test_name_2"
