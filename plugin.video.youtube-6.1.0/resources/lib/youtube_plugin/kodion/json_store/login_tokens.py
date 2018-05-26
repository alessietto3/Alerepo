# -*- coding: utf-8 -*-
"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

from . import JSONStore


class LoginTokenStore(JSONStore):
    def __init__(self):
        JSONStore.__init__(self, 'access_manager.json')

    def set_defaults(self):
        data = self.get_data()
        if 'access_manager' not in data:
            data = {'access_manager': {'users': {'0': {'access_token': '', 'refresh_token': '', 'token_expires': -1, 'last_key_hash': '', 'name': 'Default'}}}}
        if 'users' not in data['access_manager']:
            data['access_manager']['users'] = {'0': {'access_token': '', 'refresh_token': '', 'token_expires': -1, 'last_key_hash': '', 'name': 'Default'}}
        if '0' not in data['access_manager']['users']:
            data['access_manager']['users']['0'] = {'access_token': '', 'refresh_token': '', 'token_expires': -1, 'last_key_hash': '', 'name': 'Default'}
        if 'current_user' not in data['access_manager']:
            data['access_manager']['current_user'] = '0'
        if 'last_origin' not in data['access_manager']:
            data['access_manager']['last_origin'] = 'plugin.video.youtube'

        # clean up
        if data['access_manager']['current_user'] == 'default':
            data['access_manager']['current_user'] = '0'
        if 'access_token' in data['access_manager']:
            del data['access_manager']['access_token']
        if 'refresh_token' in data['access_manager']:
            del data['access_manager']['refresh_token']
        if 'token_expires' in data['access_manager']:
            del data['access_manager']['token_expires']
        if 'default' in data['access_manager']:
            if (data['access_manager']['default'].get('access_token') or
                 data['access_manager']['default'].get('refresh_token')) and \
                (not data['access_manager']['users']['0'].get('access_token') and
                 not data['access_manager']['users']['0'].get('refresh_token')):
                if 'name' not in data['access_manager']['default']:
                    data['access_manager']['default']['name'] = 'Default'
                data['access_manager']['users']['0'] = data['access_manager']['default']
            del data['access_manager']['default']
        # end clean up

        self.save(data)
