#
# This file is part of the bladeRF-net project
#
# Copyright (C) 2020 Nuand LLC
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

from flask import Flask
from flask import request
from flask import send_from_directory
from pathlib import Path
app = Flask(__name__)
from datetime import datetime

@app.route('/images/<path:filename>')
def show_image(filename):
    return send_from_directory('images/', filename)

@app.route('/')
def hello_world():
    sz = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    ret = "<center>\n"
    if Path("./images/birb.png").is_file():
        ret += "<img src=\"/images/birb.png\" width=\"350\" height=\"350\"><br />\n"
    ret += "Welcome to bladeRF-net!<br />\n"
    ret += "It is currently: {}<br />\n".format(sz)
    ret += "Your assigned IP address is: {}<br />\n".format(request.remote_addr)
    ret += "For more information about the bladeRF-wiphy project go to the <a href=\"https://github.com/Nuand/bladeRF-wifi.git\">Github!</a>"
    return ret

app.run(host='0.0.0.0', port=5000)


