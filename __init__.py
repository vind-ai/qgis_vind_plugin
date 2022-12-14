# -*- coding: utf-8 -*-
"""
/***************************************************************************
 VindTechnologies
                                 A QGIS plugin
 Plugin synching QGIS project with Vind projects
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-08-30
        copyright            : (C) 2022 by Vind Technologies
        email                : support@vind.ai
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load VindTechnologies class from file VindTechnologies.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .vind_technologies import VindTechnologies
    return VindTechnologies(iface)
