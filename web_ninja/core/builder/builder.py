import logging
from pathlib import Path
from typing import List

from web_ninja.core.template.base import BaseTemplate

logger = logging.getLogger(__name__)


class Builder:
    def __init__(self, path: Path):
        self.path = path
        self.templates: List[BaseTemplate] = []

    def add_template(self, template: BaseTemplate):
        self.templates.append(template)

    def build(self):
        for template in self.templates:
            logger.info(f"Generating {template.__class__.__name__}...")
            template.generate()
