from pathlib import Path
from web_ninja.core.template.module import ModuleTemplate



class MessageBrokerTemplate(ModuleTemplate):
    def __init__(self, base_dir: Path) -> None:
        super().__init__(base_dir)
        self.child_dirs = [Path("message_broker")]

        message_broker_base = ""
        with open(Path("web_ninja/templates/message_broker.py"), "r") as f:
            message_broker_base = f.read()
        message_broker_celery = ""
        with open(Path("web_ninja/modules/message_broker/celery.py"), "r") as f:
            message_broker_celery = f.read()

        self.module_files = [
            {
                "child_path": Path("message_broker/__init__.py"),
                "content": "",
            },
            {
                "child_path": Path("message_broker/base.py"),
                "content": message_broker_base,
            },
            {
                "child_path": Path("message_broker/celery.py"),
                "content": message_broker_celery,
            }
        ]
