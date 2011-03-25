from zope import i18nmessageid
messageFactory = i18nmessageid.MessageFactory('makina.maintenance')
_ = messageFactory

tracker_credits_label = _(u"tracker_credits_label",
                                    default=u"Available maintenance credits")
tracker_credits_desc  = _(u"tracker_credits_desc",
                                    default=u"The amount of credits you can spend on maintenance")

issue_credits_label = _(u"issue_credits_label",
                                    default=u"Needed maintenance credits")
issue_credits_desc  = _(u"issue_credits_desc",
                                    default=u"The amount of credits needed to solve that issue")
