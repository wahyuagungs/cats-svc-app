from flask import Blueprint, request, json, redirect
from utils import authenticated_resource, wrapper, get_user_id, get_current_date
from werkzeug.utils import secure_filename
import os
from flask import current_app
from models.base import db
from models.module import Module
from exception.appexception import AppException
from exception.appexceptioncode import AppExceptionCode
from itertools import product
from datetime import datetime
# import dateutil.parser
import re

module_controller = Blueprint('module_controller', __name__)


@module_controller.route('/api/module/list')
@wrapper
def get_module():
    data = Module.get_list()
    return [d.as_dict() for d in data]


@module_controller.route('/api/module/code')
@wrapper
def get_module_by_kd():
    kd_module = request.args.get('kd_module')
    module = Module.get(kd_module)
    if module is None:
        raise AppException(AppExceptionCode.NOT_FOUND_ERROR)
    if not module.has_loaded:
        raise AppException(AppExceptionCode.ILLEGAL_ARGUMENT)

    return module


@module_controller.route('/api/module/search')
@wrapper
def get_module_by_name():
    name = request.args.get('name')
    search = "%{}%".format(name)
    modules = Module.query.filter(Module.name.ilike(search)).all()
    return [d.as_dict() for d in modules]



