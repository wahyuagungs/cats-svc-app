from flask import Blueprint, request, json, redirect
from utils import authenticated_resource, wrapper, get_user_id, get_current_date
from werkzeug.utils import secure_filename
import os
from flask import current_app
from models.base import db
from models.counterpart import Counterpart
from exception.appexception import AppException
from exception.appexceptioncode import AppExceptionCode
from itertools import product
from datetime import datetime
# import dateutil.parser
import re

entity_controller = Blueprint('entity_controller', __name__)


@entity_controller.route('/api/entity/list')
@wrapper
def get_entity():
    data = Counterpart.get_list()
    return [d.as_dict() for d in data]


@entity_controller.route('/api/entity/search')
@wrapper
def get_entity_by_name():
    name = request.args.get('name')
    search = "%{}%".format(name)
    data = Counterpart.query.filter(Counterpart.entity_name.ilike(search)).all()
    return [d.as_dict() for d in data]


