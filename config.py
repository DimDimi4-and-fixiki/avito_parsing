from __future__ import annotations

import pathlib

from environs import Env


PROJECT_DIR = pathlib.Path(__file__).parent

env_reader = Env()
env_reader.read_env()

AVITO_URL: str = env_reader.str('AVITO_URL', default='')
