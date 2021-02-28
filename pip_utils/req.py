def parse_requirements(filename):
    """Parse requirement file with python pip packages versions.

    Args:
        filename (str): Path to file with python pip packages versions.

    Returns:
        list: List of packages for installation.
    """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]
