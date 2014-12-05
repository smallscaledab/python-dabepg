#===============================================================================
# Python DAB EPG API - Serialize/Deserialize To/From objects to XML/Binary as per
# ETSI specifications TS 102 818 (XML Specification for DAB EPG) and TS 102 
# 371 (Transportation and Binary Encoding Specification for EPG).
# 
# Copyright (C) 2010 Global Radio
# 
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# 
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
#===============================================================================

from dabepg import *
from dabepg.xml import marshall
import datetime


info = GroupInfo(originator='BBC', created=datetime.datetime(2001, 02, 28, 0, 0, 0, 0))

group = ProgrammeGroup(1000, ProgrammeGroup.SHOW, 206, crid://www.bbc.co.uk/WorldwideGroup)
group.names.append(MediumName("Gilles Peterson"))
group.names.append(LongName("Gilles Peterson: Worldwide"))
group.media.append(ShortDescription("Worldwide: Global beats."))
group.media.append(LongDescription("Worldwide: Music from the back room of Club Radio 1."))
group.genres.append("urn:tva:metadata:cs:ContentCS:2002:3.6.7")
group.genres.append("urn:tva:metadata:cs:ContentCS:2002:3.6.8")
group.genres.append("urn:tva:metadata:cs:FormatCS:2002:2.5")
group.genres.append("urn:tva:metadata:cs:IntentionCS:2002:1.1")
group.genres.append("urn:tva:metadata:cs:ContentCS:2002:3.6.9")
group.memberships.append(Membership(100, "crid://www.bbc.co.uk/Radio1_Series"))

gi.groups.append(group)


print marshall(info, indent='\t')