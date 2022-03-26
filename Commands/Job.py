from abc import ABC, abstractmethod


#
#
# Here I tried to realize Object oriented programming pattern: 'Command'
#
#

class List(ABC):
    """
    It is an Abstract class Command which defines \
    single method 'list' which display job`s list
    """

    @abstractmethod
    def list(self) -> list:
        """This method should return job`s list"""

        ...


class Create(ABC):
    """
    It is an Abstract class Create which defines \
    single method 'create' which create new job

    """

    @abstractmethod
    def create(self, job: str = 'daily/month/year') -> str:
        """
        This method should create new job and \
        display appropriate info message for user \
        like == Job with name 'some_job' was \
        successfully/unsuccessfully created/not created

        !!!
        To execute this method you have handover argument job
        !!!

        Required argument 'job':

        You have to put one of this values

            job=daily
            job=month
            job=year

        """
        ...
