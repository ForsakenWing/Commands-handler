from abc import ABC, abstractmethod


#
#
# Here I tried to realize Object oriented programming pattern: 'Command'
#
#


class Deploy(ABC):
    """
    It is an Abstract class Command which defines \
    single method 'deploy' which deploy service to server
    """

    @abstractmethod
    def deploy(self) -> list:
        """
        This method should deploy required service and \
        display appropriate info message for user \
        like == service with name 'some_service' was \
        successfully/unsuccessfully deployed/not deployed


        !!!
        To execute this method you have handover arguments:

        service
        version

        !!!

        Required arguments 'service, version':

        You have to put one of this values

            service=app
            service=web
            service=desktop

            version=1
            version=2
            version3

        """

        ...


class Config(ABC):
    """
    It is an Abstract class Command which defines \
    single method 'config' which display service configuration
    """

    @abstractmethod
    def config(self):
        """
        This method should display service configuration info
        """
        ...


class Template(ABC):
    """
    It is an Abstract class Command which defines \
    single method 'template' which.... What is supposed to do??
    """

    @abstractmethod
    def template(self):
        """
        Useful info about this method
        """
        ...
