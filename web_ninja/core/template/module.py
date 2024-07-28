from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List

from jinja2 import Template

from web_ninja.core.template.base import BaseTemplate
from web_ninja.utils.directory import create_directory, create_file


@dataclass
class ModuleFile:
    child_path: Path
    content: str


class ModuleTemplate(BaseTemplate[Dict[str, Any]]):
    def __init__(self, base_dir: Path) -> None:
        self.base_dir = base_dir
        self.child_dirs: List[Path] = []
        self.module_files: List[ModuleFile] = []

    def render(self, context: Dict[str, Any]) -> None:
        for module_file in self.module_files:
            module_file.content = Template(module_file.content).render(context)

    def generate(self):
        for child_dir in self.child_dirs:
            create_directory(self.base_dir / child_dir)
        for module_file in self.module_files:
            create_file(self.base_dir / module_file.child_path, module_file.content)
