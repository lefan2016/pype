"""
Requires:
    None
Provides:
    context -> deadlienRestUrl (str)
"""

import pyblish.api
from pype.api import get_deadline_url


class CollectDeadlineRestUrl(pyblish.api.ContextPlugin):
    """This plugin is getting deadline rest url into context"""

    label = "Collect Deadline Rest Url"
    order = pyblish.api.CollectorOrder

    def process(self, context):
        dl_rest_url = get_deadline_url()

        context.data["deadlienRestUrl"] = dl_rest_url