#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Roman Bobrovskiy

from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)
