# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    # ------------------------------------------------------
    # ACTIONS
    # ------------------------------------------------------
    def action_show_delivery_details(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("trescloud_test.action_view_delivery_details")
        action['domain'] = [('account_move_id', '=', self.id)]
        action['context'] = {
            'default_account_move_id': self.id,
            'create': False,
            'edit': False,
        }
        return action

    def action_post(self):
        """
        Sobrescribimos el método action_post para que, al confirmar una factura, se cree un detalle de entrega
        asociado a la factura. Esto es útil para registrar la información de entrega relacionada con la factura.
        """
        account_move_lines = self.line_ids
        delivery_detail_lines = []
        for line in account_move_lines:
            delivery_detail_lines.append((0, 0, {
                'qty': line.quantity,
                'uom_id': line.product_uom_id.id,
            }))
        delivery_detail_values = {
            'account_move_id': self.id,
            'picking_id': self.sale_order_id.picking_ids,
            'invoiced': False,
            'delivery_detail_line_ids': delivery_detail_lines,
        }
        self.env['delivery.detail'].create(delivery_detail_values)
        return super(AccountMove, self).action_post()
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

