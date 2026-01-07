from datetime import datetime
from pathlib import Path
import threading


class LazyFileAuditManager:
    _instance = None
    _instance_lock = threading.Lock()

    def __new__(cls):
        with cls._instance_lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)

    def configure(self, file_path: str):
        if hasattr(self, "_file_path"):
            raise RuntimeError("File path already defined.")
        
        self._file_path = Path(file_path)
        self._write_lock = threading.Lock()

    def log(self, message: str):
        if not hasattr(self, "_file_path"):
            raise RuntimeError("File path not defined.")
        
        timestamp = datetime.now(tz="utc")

        line = f"{timestamp} - {message}\n"

        with self._write_lock:
            with self._file_path.open("a", encoding="utf-8") as f:
                f.write(line)

