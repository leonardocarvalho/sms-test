import setuptools


setuptools.setup(
    name="geekie-sms",
    version="1.0",
    url="http://www.geekie.com.br",
    maintainer="Geekie",
    maintainer_email="geekie@geekie.com.br",
    packages=["geekie"],
    namespace_packages=["geekie"],
    include_package_data=True,
    zip_safe=False,
    setup_requires=["setuptools_git==1.0b1"],
    install_requires=[
        "pyramid==1.4.2",
        "pyramid_debugtoolbar==1.0.6",
        "PasteDeploy==1.5.0",
        "pyramid_tm==0.7",
        "requests==2.1.0",
        "setuptools-git==1.0b1",
        "waitress==0.8.5",
        "twilio",
    ],
    entry_points={
        "paste.app_factory": "main = geekie.sms.main:main",
    }
)
