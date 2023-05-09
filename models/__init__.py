#!/usr/bin/python3
"""This is the __init__ file for the models package"""
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
