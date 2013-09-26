
# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution    
#    Copyright (C) 2004-2010 Tiny SPRL (http://tiny.be). All Rights Reserved
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

{
    "name": "CRM Extension", 
    "version": "1.0",
    "depends": ["base", "crm"],
    "author": "Radmas Technologies S.L.",
    "category": "CRM",
    "description": """
        Este módulo extiende la funcionalidad base del módulo de CRM de OpenERP.
        
        Se han añadido las siguientes funcionalidades:
        
        Categorías: 
        - Añadido campo Padre para poder anidar las categorías. Este campo aparece en todas las vistas, y se permite filtrado y agrupación
        - Añadida vista jerárquica de categorías, donde se puede visualizar todo el árbol de categorías.
        
        Iniciativas:
        - Se ha añadido el campo Categoría al listado.
        - El nombre que se muestra de la Categoría corresponde a la estructura jerárquica de la categoría (Padre / Hijo).
    """,
    "init_xml": [],
    'update_xml': ['crm_case_categ_ext_view.xml',
                   'crm_lead_view_ext.xml'],
    'demo_xml': [],
    'installable': True,
    'active': False,
#    'certificate': 'certificate',
}
