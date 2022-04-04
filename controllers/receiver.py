def accept(event_as_json):
    """
    Accepts new data from the API.

    Args:
        event_as_json (str): event data as a json string.

    Returns:
        True if event is queued successfully, False otherwise.
    """
    event = _parse_event(event_as_json)
    validation = _validate(event)
    sent = False

    if validation.get('success'):
        sent = _send_to_queue(event)
    else:
        sent = _send_to_error_queue(event)

    return sent


def _send_to_error_queue(event_as_json, validation):
    """
    Send event data and its respective validation results to a specific queue in order to extract measures later.

    Args:
        event_as_json (str): event data as a json string.
        validation (): dict that contains validation results, including error messages.

    Returns:
        True in case of success, False otherwise.
    """
    pass


def _send_to_queue(event):
    """
    Send a new event to a queue in order to process it later.

    Args:
        event (Event): a new event.

    Returns:
        True in case of success, False otherwise.
    """
    pass


def _validate(event):
    """
    Validates event data.

    Args:
        event (Event): a single event to validate

    Returns:
         a dict containing a flag indicating if validation is a success or not and error messages in case of validation
         failure.
    """
    pass


def _parse_event(event_as_json):
    """
    Build an Event instance from the given json.

    Args:
        event_as_json (str): event data as a json string.

    Returns:
        an Event instance.
    """
    pass
