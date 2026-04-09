import json
from functools import wraps


def to_format(func):
    """
    Converts the return value of a function to different output formats.

    The decorator wraps a function and transforms its return value into JSON, XML, or YAML format
    based on the user_format parameter passed to the decorated function. If no format is specified,
    JSON format is used by default.

    Args:
        func: The function to be decorated. The function should return data that can be serialized
              to JSON, XML, or YAML formats.

    Returns:
        A wrapper function that accepts a user_format keyword argument ('json', 'xml', or 'yaml')
        and returns the serialized output in the requested format.

    Raises:
        ValueError: If an unsupported format is specified
    """

    @wraps(func)
    def wrapper(*args, user_format=None, **kwargs):
        user_format.lower()
        result = func(*args, **kwargs)
        match user_format:
            case 'json' | None:
                return json.dumps(
                    result,
                    ensure_ascii=False,
                    indent=2)

            case 'xml':
                root = ET.Element('data')

                for item in result:
                    el = ET.SubElement(root, 'el')
                    if isinstance(item, dict):
                        for key, value in item.items():
                            child = ET.SubElement(el, key)
                            child.text = str(item)

                    else:
                        el.text = str(item)

                return ET.tostring(root, encoding='unicode')

            case 'yaml':
                return yaml.safe_dump(
                    result,
                    allow_unicode=True,
                    sort_keys=False
                )

            case _:
                raise ValueError('Unknown')

    return wrapper




