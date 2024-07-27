import logging
import os
from pathlib import Path

logger = logging.getLogger(__name__)


def create_directory(path: Path):
    try:
        path.mkdir(parents=True, exist_ok=True)
        logger.info(f"Directory created at: {path}")
    except PermissionError:
        logger.info(
            f"Permission denied: Cannot create {path}. Attempting to change permissions..."
        )
        try:
            os.chmod(path.parent, 0o777)
            path.mkdir(parents=True, exist_ok=True)
            logger.info(f"Directory created at: {path}")
        except Exception as e:
            logger.info(f"Failed to create directory: {e}")


def create_file(file_path: Path):
    try:
        with open(file_path, "w") as file:
            file.write("Hello, World!")
        logger.info(f"File created at: {file_path}")
    except PermissionError:
        logger.info(
            f"Permission denied: Cannot write to {file_path}. Attempting to change permissions..."
        )
        try:
            os.chmod(file_path.parent, 0o777)
            with open(file_path, "w") as file:
                file.write("Hello, World!")
            logger.info(f"File created at: {file_path}")
        except Exception as e:
            logger.info(f"Failed to create file: {e}")
