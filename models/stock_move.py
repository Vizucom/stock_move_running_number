# -*- coding: utf-8 -*-
from openerp import models, fields, api


class StockMove(models.Model):

    _inherit = 'stock.move'

    @api.one
    def _get_running_number(self):
        '''Assigns a running number to the stock move, starting from 1 onwards '''

        '''Get all lines related to the current Picking. '''
        move_lines = self.search(args=[('picking_id', '=', self.picking_id.id)])

        i = 1
        for line in move_lines:
            if line.id == self.id:
                self.running_number = i
                break
            i += 1

    running_number = fields.Integer('Running Number', compute=_get_running_number)
