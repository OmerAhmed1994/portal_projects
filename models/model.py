# -*- coding: utf-8 -*-
import logging
from odoo.osv import expression
import re
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
from odoo.addons import decimal_precision as dp

_logger = logging.getLogger(__name__)

class ResUsers(models.Model):
    _inherit = 'res.users'

    user_parent_id = fields.Many2one('res.users', index=True, ondelete='cascade')
    user_child_ids = fields.One2many('res.users', 'user_parent_id')
    all_child_ids = fields.Many2many('res.users',compute='_compute_all_child_ids')
   
    def get_leaf_nodes(self):
        leafs = []
        def _get_leaf_nodes(node):
            if node is not None:
                for n in node.user_child_ids:
                    leafs.append(n.id)
                    _get_leaf_nodes(n)
        _get_leaf_nodes(self)
        return leafs
    
    def _compute_all_child_ids(self):
        for user in self:
            user.all_child_ids = user.get_leaf_nodes()

    @api.constrains('user_parent_id')
    def _check_parent_recursion(self):
        if not self._check_recursion():
            raise ValidationError(_('You cannot create recursive user.'))
        return True
