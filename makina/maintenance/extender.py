#use schema extender to extend poi
from zope import component
from zope import interface
from zope.interface import implements
from Products.Archetypes import public as atapi
from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender import interfaces as extenderfaces

from Products.Poi import interfaces as poifaces

from makina.maintenance import interfaces
from makina.maintenance import i18n

class MaintenanceCredit(ExtensionField, atapi.IntegerField):
    """Define a unit associated to each issue and a global amount available
    on the tracker"""


class TrackerExtender(object):
    """Include available maintenance unit on tracker"""
    component.adapts(poifaces.ITracker)
    implements(extenderfaces.ISchemaExtender,
               extenderfaces.IBrowserLayerAwareExtender)

    layer = interfaces.IMakinaMaintenanceLayer

    fields = [MaintenanceCredit("credits",
                    accessor="getCredits",
                    languageIndependent = True,
                    schemata="default",
                    widget = atapi.IntegerWidget(
                        label=i18n.tracker_credits_label,
                        description=i18n.tracker_credits_desc,
                    ),
                )
             ]
    def __init__(self, context):
        self.context = context

# if you want to manange order, use  IOrderableSchemaExtender with
#    def getOrder(self, schematas):
#        """ Manipulate the order in which fields appear.
#        
#        @param schematas: Dictonary of schemata name -> field lists
#        
#        @return: Dictionary of reordered field lists per schemata.
#        """
#        schematas["properties"] = ['effectiveDate', 'revisitDate', 'expirationDate', 'creation_date', 'modification_date']
#        
#        return schematas

    def getFields(self):
        """
        @return: List of new fields we contribute to content.
        """
        return self.fields

class IssueExtender(object):
    component.adapts(poifaces.IIssue)
    implements(extenderfaces.ISchemaExtender,
               extenderfaces.IBrowserLayerAwareExtender)

    layer = interfaces.IMakinaMaintenanceLayer

    fields = [MaintenanceCredit("credits",
                    accessor="getCredits",
                    languageIndependent = True,
                    schemata="default",
                    widget = atapi.IntegerWidget(
                        label=i18n.issue_credits_label,
                        description=i18n.issue_credits_desc,
                    ),
                )
             ]
    def __init__(self, context):
        self.context = context

    def getFields(self):
        """
        @return: List of new fields we contribute to content.
        """
        return self.fields

