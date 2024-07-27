from pathlib import Path
from typing import Any, Dict

from web_ninja.core.template.directory import DirectoryTemplate


class LayeredArchitectureTemplate(DirectoryTemplate[Dict[str, Any]]):
    def __init__(self, path: Path) -> None:
        super().__init__(path)
        self.child_dirs = [
            path / "api",
            path / "api/v1",
            path / "api/v1/endpoints",
            path / "service",
            path / "repository",
            path / "model",
            path / "dao",
            path / "schema",
            path / "external",
            path / "extension",
        ]
        self.child_files = [
            path / "api/__init__.py",
            path / "api/v1/__init__.py",
            path / "api/v1/endpoints/__init__.py",
            path / "service/__init__.py",
            path / "repository/__init__.py",
            path / "model/__init__.py",
            path / "dao/__init__.py",
            path / "schema/__init__.py",
            path / "external/__init__.py",
            path / "extension/__init__.py",
        ]

    def render(self, context: Dict[str, Any]) -> None:
        pass
