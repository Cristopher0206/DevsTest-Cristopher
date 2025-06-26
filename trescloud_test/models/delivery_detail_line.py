# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class DeliveryDetailLine(models.Model):
    _name = 'delivery.detail.line'

    # ------------------------------------------------------
    # ACTIONS
    # ------------------------------------------------------

    # ------------------------------------------------------
    # CRUD METHODS
    # ------------------------------------------------------

    # ------------------------------------------------------
    # COMPUTE METHODS
    # ------------------------------------------------------

    # ------------------------------------------------------
    # CONSTRAINTS AND VALIDATIONS
    # ------------------------------------------------------

    # ------------------------------------------------------
    # ONCHANGE METHODS
    # ------------------------------------------------------

    # ------------------------------------------------------
    # OTHER METHODS
    # ------------------------------------------------------

    # ------------------------------------------------------
    # VARIABLES
    # ------------------------------------------------------

    delivery_detail_id = fields.Many2one(
        'delivery.detail',
    )
    qty = fields.Float(
        string='Cantidad',
        help="Cantidad de producto en este detalle de entrega.",
    )
    uom_id = fields.Many2one(
        'uom.uom',
        string='Unidad de Medida',
    )
