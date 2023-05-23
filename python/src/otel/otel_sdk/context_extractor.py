from opentelemetry.propagate import get_global_textmap


def event_context_extractor(lambda_event):
    """Method to extract context from the lambda event.
    See more:
    https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format
    Args:
        lambda_event: user-defined, so it could be anything, but this
            method counts on it being a map with a 'headers' key
    Returns:
        A Context with configuration found in the event.
    """
    headers = None
    try:
        headers = lambda_event["request"]["headers"]
    except (TypeError, KeyError):
        pass
    if not isinstance(headers, dict):
        headers = {}
    return get_global_textmap().extract(headers)