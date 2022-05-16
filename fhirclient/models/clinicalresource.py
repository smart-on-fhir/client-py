from . import domainresource


class ClinicalResource(domainresource.DomainResource):
    def get_date(self, return_all=False):
        """
        gets date(s) relevant to the resource
        :param return_all: if True, return all dates in a descriptive dictionary,
         else return only a select relevant date
        :return: if return_all=True: (datetime: date, dict: all_dates)
        """
        raise NotImplementedError()