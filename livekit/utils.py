def camel_case_dict(data) -> dict:
    """
    Return dictionary with keys converted from snake_case to camelCase

    Example:
        dataclasses.asdict(my_data, dict_factory=camel_case_dict)
    """
    return {
        "".join(
            word if i == 0 else word.title() for i, word in enumerate(key.split("_"))
        ): value
        for key, value in data
        if value is not None
    }
