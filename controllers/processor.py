def process(event):
    """
    Process a new event read from the queue.

    Args:
        event (Event): a event read from the new events queue.

    Returns:
        True if succes, False otherwise.
    """
    measure = _extract_measure(event)
    entities = _extract_entities(event)

    return _save(measure, entities)


def _save(measure, entities):
    """
    Saves measure and relate it to the given entities. To do so, it will follow
    the Star-Schema model as follows:
    - each measure have its own storage
    - a new record will be created in this storage
    - this new record will be related to entities based on foreign keys.

    Args:
        measure (MEASURE): indicates where the new record should be saved.
        entities (list of Entity): indicates who is related to the new record.

    Returns:
        True if success, False otherwise.
    """
    pass


def _extract_measure(event):
    """
    Returns what is the measure related to the given event based on payload.

    Args:
        event (Event): an event instance.

    Returns:
        an instance of MEASURES.
    """
    pass


def _extract_entities(event):
    """
    Return a list of entities present in a given event.

    Args:
        event (Event): an event instance.

    Returns:
        a list of Entity instances.
    """
    pass
