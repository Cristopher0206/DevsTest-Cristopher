# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'


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
