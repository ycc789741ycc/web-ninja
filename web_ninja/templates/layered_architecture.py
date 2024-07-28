from pathlib import Path
from typing import Any, Dict

from web_ninja.core.template.directory import DirectoryTemplate


class LayeredArchitectureTemplate(DirectoryTemplate[Dict[str, Any]]):
    def __init__(self, base_dir: Path) -> None:
        super().__init__(base_dir)
        self.child_dirs = [
            base_dir / "api",
            base_dir / "api/v1",
            base_dir / "api/v1/endpoints",
            base_dir / "service",
            base_dir / "repository",
            base_dir / "model",
            base_dir / "dao",
            base_dir / "schema",
            base_dir / "external",
            base_dir / "extension",
        ]
        self.child_files = [
            base_dir / "api/__init__.py",
            base_dir / "api/v1/__init__.py",
            base_dir / "api/v1/endpoints/__init__.py",
            base_dir / "service/__init__.py",
            base_dir / "repository/__init__.py",
            base_dir / "model/__init__.py",
            base_dir / "dao/__init__.py",
            base_dir / "schema/__init__.py",
            base_dir / "external/__init__.py",
            base_dir / "extension/__init__.py",
        ]

    def render(self, context: Dict[str, Any]) -> None:
        pass
