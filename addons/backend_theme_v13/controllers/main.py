# -*- coding: utf-8 -*-
# Copyright 2016, 2019 Openworx
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

import base64
from odoo.http import Controller, request, route
from werkzeug.utils import redirect
import random

DEFAULT_IMAGE = '/backend_theme_v13/static/src/img/material-background.png'
SCCC_IMAGE_1 = '/backend_theme_v13/static/src/img/home-h-training.jpg'
SCCC_IMAGE_2 = '/backend_theme_v13/static/src/img/home-h-individual.jpg'
SCCC_IMAGE_3 = '/backend_theme_v13/static/src/img/home-h-couple.jpg'
random_images = [SCCC_IMAGE_1, SCCC_IMAGE_2, SCCC_IMAGE_3]

class DasboardBackground(Controller):

    @route(['/dashboard'], type='http', auth='user', website=False)
    def dashboard(self, **post):
        user = request.env.user
        company = user.company_id
        if company.dashboard_background:
            image = base64.b64decode(company.dashboard_background)
        else:
            return redirect(random.choice(random_images))

        return request.make_response(
            image, [('Content-Type', 'image')])