# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

import jwt
import time


class SecurityTokenContainer(object):
    def __init__(self, session_key_supplier, security_token):
        self.security_token = security_token
        self.session_key_supplier = session_key_supplier
        self.jwt = jwt.decode(jwt=security_token, verify=False)

    def get_jwt(self):
        return self.jwt

    def valid(self):
        return not self._expired()

    def _expired(self):
        # The exp key which PyJWT returns is in epoch seconds
        time_now = int(time.time())
        return time_now > self.jwt['exp']
