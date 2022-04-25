
import os

from flask import Blueprint, request

from core import video_core

video = Blueprint("video", __name__)
