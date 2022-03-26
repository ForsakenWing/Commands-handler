import argparse
import sys


class CustomFormatter(argparse.RawDescriptionHelpFormatter,
                      argparse.ArgumentDefaultsHelpFormatter):
    pass


def parse_args(args=sys.argv[1:]):
    """Parse arguments."""
    parser = argparse.ArgumentParser(
        description=sys.modules[__name__].__doc__,
        formatter_class=CustomFormatter)

    service_group = parser.add_argument_group("service commands")
    service_group.add_argument("deploy")
    service_group.add_argument("config")
    service_group.add_argument("template")

    job_group = parser.add_argument_group("job commands")
    job_group.add_argument("list")
    job_group.add_argument("create")

    return parser.parse_args(args)


options = parse_args()
for n in range(options.start, options.end + 1):
    ...
