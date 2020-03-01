def transform(legacy_data: dict) -> dict:
    """
    Extract-Transform-Load (ETL) is a fancy way of saying,
    "We have some crufty, legacy data over in this system,
    and now we need it in this shiny new system over here,
    so we're going to migrate this."
    :param legacy_data:
    :return:
    """
    data = dict()
    for key in legacy_data:
        for char in legacy_data[key]:
            data[char.lower()] = key

    return data
