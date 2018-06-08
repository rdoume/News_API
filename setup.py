# -*- coding: utf-8 -*-
import os

import setuptools

from pip import download
from pip import req


HERE = os.path.abspath(os.path.dirname(__file__))


def get_requirements(reqfile):
    path = os.path.join(HERE, reqfile)
    deps = set()
    for dep in req.parse_requirements(path, session=download.PipSession()):
        try:
            # Pip 8.1.2 Compatible
            specs = ",".join("".join(str(spec)) for spec in dep.req.specifier)
        except AttributeError:
            # Pip 1.5.4 Compatible
            specs = ",".join("".join(spec) for spec in dep.req.specs)
        requirement = "{name}{extras}{specs}".format(
            name=dep.name,
            extras=(
                "[{extras}]".format(extras=",".join(dep.extras)) if dep.extras else ""
            ),
            specs=specs,
        )

        deps.add(requirement)
    return list(deps)


setuptools.setup(
    name="News_API",
    description="API for the Qwant news cluster. The cluster is currently hosted on a vespa-engine setup",
    version="0.0.1",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=get_requirements("requirements/requirements.txt"),
    tests_require=get_requirements("requirements/test-requirements.txt"),
    author="Robin",
    author_email="robin@qwantresearch.com",
    url="qwant.com/news",
)
