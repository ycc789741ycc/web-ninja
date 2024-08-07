from pathlib import Path
from typing import List, TypeVar

from web_ninja.core.template.base import BaseTemplate
from web_ninja.utils.directory import create_directory, create_file

T = TypeVar("T")


class DirectoryTemplate(BaseTemplate[T]):
    def __init__(self, base_dir: Path) -> None:
        self.base_dir = base_dir
        self.child_dirs: List[Path] = []
        self.child_file_paths: List[Path] = []

    def generate(self):
        for child_dir in self.child_dirs:
            create_directory(child_dir)
        for child_file_path in self.child_file_paths:
            create_file(child_file_path)
