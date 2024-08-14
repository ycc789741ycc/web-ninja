from pathlib import Path
from web_ninja.core.template.module import ModuleTemplate, ModuleFile


class MessageBrokerTemplate(ModuleTemplate):
    def __init__(self, base_dir: Path) -> None:
        super().__init__(base_dir)
        self.child_dirs = [Path("message_broker")]

        message_broker_base = ""
        with open(Path("web_ninja/modules/message_broker/base.py"), "r") as f:
            message_broker_base = f.read()
        message_broker_celery = ""
        with open(Path("web_ninja/modules/message_broker/celery.py"), "r") as f:
            message_broker_celery = f.read()
        docker_compose_file = ""
        with open(Path("web_ninja/modules/message_broker/docker-compose.yml"), "r") as f:
            docker_compose_file = f.read()

        self.module_files = [
            ModuleFile(
                child_path=Path("message_broker/__init__.py"),
                content=""
            ),
            ModuleFile(
                child_path=Path("message_broker/base.py"),
                content=message_broker_base,
            ),
            ModuleFile(
                child_path=Path("message_broker/celery.py"),
                content=message_broker_celery,
            ),
            ModuleFile(
                child_path=Path("message_broker/docker-compose.yml"),
                content=docker_compose_file,
            ),
        ]
