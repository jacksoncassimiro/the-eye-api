from enum import Enum


class Event:
    """
    Represents an event received from the API.
    """

    def __init__(self, session_id, category, name, timestamp, payload):
        self.session_id = session_id
        self.category = category
        self.name = name
        self.timestamp = timestamp
        self.payload = payload


class PageViewPayload:
    """
    Encapsulates data related to a page view.
    """

    def __init__(self, host, path):
        self.host = host
        self.path = path


class PageInteractionPayload:
    """
    Encapsulates data related to an interaction with a page element.
    """

    def __init__(self, host, path, element):
        self.host = host
        self.path = path
        self.element = element


class FormInteractionPayload:
    """
    Encapsulates data that represents a form submission.
    """

    def __init__(self, host, path):
        self.host = host
        self.path = path


class ErrorEvent:
    """
    Represents an event that failed during validation.
    """

    def __init__(self, event_as_json, validation, timestamp):
        self.event_as_json = event_as_json
        self.validation = validation
        self.timestamp = timestamp


class Entity:
    """
    Represents who is related to a given event, like an application, a page, a speficic form, a page element
    (button, link), etc.
    """

    def __init__(self, entity_id):
        self.entity_id = entity_id


class MEASURES(Enum):
    """
    Represents what is possible to count or measure from the events, like page views, interactions with a page element
    or form submissions.
    """
    PAGE_VIEW = 1
    PAGE_INTERACTION = 2
    FORM_INTERACTION = 3
