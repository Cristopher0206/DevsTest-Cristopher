# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class DeliveryDetail(models.Model):
    _name = 'delivery.detail'

    # ------------------------------------------------------
    # ACTIONS
    # ------------------------------------------------------

    # ------------------------------------------------------
    # CRUD METHODS
    # ------------------------------------------------------
    # @api.model_create_multi

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

    account_move_id = fields.Many2one(
        'account.move',
        string='Factura',
        help="Factura asociada a este detalle de entrega."
    )
    picking_id = fields.Many2one(
        'stock.picking',
        string='Transferencia',
        help="Transferencia asociada a este detalle de entrega."
    )
    invoiced = fields.Boolean(
        string='Facturado',
        default=False,
        help="Indica si el detalle de la orden ha sido facturado por completo."
    )
    delivery_detail_line_ids = fields.One2many(
        'delivery.detail.line',
        'delivery_detail_id',
    )