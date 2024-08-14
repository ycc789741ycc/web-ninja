import logging
import subprocess
from pathlib import Path
from typing import Optional

from web_ninja.core.template.module import ModuleFile, ModuleTemplate

logger = logging.getLogger(__name__)


class DevToolsTemplate(ModuleTemplate):
    def __init__(self, base_dir: Path) -> None:
        super().__init__(base_dir)

        makefile = ""
        with open(Path("web_ninja/modules/dev_tools/mk_template.j2"), "r") as f:
            makefile = f.read()
        pre_commit_config = ""
        with open(Path("web_ninja/modules/dev_tools/pre-commit.j2"), "r") as f:
            pre_commit_config = f.read()

        self.module_files = [
            ModuleFile(child_path=Path("Makefile"), content=makefile),
            ModuleFile(
                child_path=Path(".pre-commit-config.yaml"),
                content=pre_commit_config,
            ),
        ]

    def generate(self):
        super().generate()
        self._install_pre_commit_hooks()
        self._add_poetry_dev_dependency("pytest")
        self._add_poetry_dev_dependency("pylint")
        self._add_poetry_dev_dependency("black")
        self._add_poetry_dev_dependency("mypy")
        self._add_poetry_dev_dependency("isort")
        self._add_poetry_dev_dependency("bandit")

    def _install_pre_commit_hooks(self):
        try:
            subprocess.run(["pre-commit", "install"], check=True)
            logger.info("pre-commit hooks installed successfully.")
        except subprocess.CalledProcessError as error:
            logger.error(f"Install pre-commit hooks error: {str(error)}")

    def _add_poetry_dev_dependency(self, package_name: str, version: Optional[str] = None):
        try:
            command = ["poetry", "add", package_name, "--group", "dev"]
            if version:
                command.append(version)
            subprocess.run(command, check=True)
            logger.info(f"Development dependency successfully added: {package_name} {version if version else ''}")
        except subprocess.CalledProcessError as error:
            logger.error(f"An error occurred while adding the development dependency: {str(error)}")
