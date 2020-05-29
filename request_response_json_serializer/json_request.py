from datetime import datetime
from flask.globals import LocalProxy
from rest_framework.request import Request
from django.http import HttpRequest
import json


def json_request(req):
    if isinstance(req, LocalProxy):
        """flask请求"""
        init = {
            "start_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
            "ip": req.remote_addr,
            "user_agent": req.headers.get("user_agent"),
            "req_authorization": req.headers.get("authorization"),
            "url": req.url,
            "host": req.host,
            "path": req.path,
            "full_path": req.full_path,
            "web_framework": "flask",
            "method": req.method.lower(),
            "get_args": {k: v for k, v in req.args.items()},
            "post_args": {k: v for k, v in req.form.items()},
            "req_data": json.loads(req.data)
        }
    elif isinstance(req, (HttpRequest, Request)):
        """django请求"""
        init = {
            "start_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
            "ip": req.META['HTTP_X_FORWARDED_FOR'] if req.META.get('HTTP_X_FORWARDED_FOR') else req.META[
                'REMOTE_ADDR'],
            "user_agent": req.META['HTTP_USER_AGENT'],
            "req_authorization": req.META.get('HTTP_AUTHORIZATION'),
            "url": req.get_host() + req.get_full_path(),
            "host": req.get_host(),
            "path": req.path,
            "full_path": req.get_full_path(),
            "web_framework": "django",
            "method": req.method.lower(),
            "get_args": dict(req.GET),
            "post_args": dict(req.POST),
            "req_data": req.data,
        }
    else:
        return None
    return init
