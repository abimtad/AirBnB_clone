"""Initialization for package 'models' """

from models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()
