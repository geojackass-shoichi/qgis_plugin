# -*- coding: utf-8 -*-
"""
/***************************************************************************
OpenLayers Plugin
A QGIS plugin

                             -------------------
begin                : 2009-11-30
copyright            : (C) 2009 by Pirmin Kalberer, Sourcepole
email                : pka at sourcepole.ch
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

#Author@Shoichi Otomo

from weblayer import WebLayer3857


class OlChiriinMapLayer(WebLayer3857):

    emitsLoadEnd = True

    def __init__(self):
        WebLayer3857.__init__(self, groupName="Chiriin Maps", groupIcon="chiriin_icon.png",
                              name='Chiriin map', html='chiriin.html')
