import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lumibot",
    version="3.0.3",
    author="Robert Grzesik",
    author_email="rob@lumiwealth.com",
    description="Backtesting and Trading Library, Made by Lumiwealth",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Lumiwealth/lumibot",
    packages=setuptools.find_packages(),
    install_requires=[
        "polygon-api-client>=1.13.3",
        "alpaca-py>=0.13.1",
        "alpha_vantage",
        "ibapi==9.81.1.post1",
        "yfinance",
        "matplotlib>=3.3.3",
        "quandl",
        "pandas>=2.0.0,<=2.0.3",
        "pandas_datareader",
        "pandas_market_calendars>=4.3.1",
        "plotly",
        "flask>=2.2.2",
        "flask-socketio",
        "flask-sqlalchemy",
        "flask-marshmallow",
        "flask-security",
        "marshmallow-sqlalchemy",
        "email_validator",
        "bcrypt",
        "pytest",
        "scipy==1.10.1",  # Newer versions of scipy are currently causing issues
        "ipython",  # required for quantstats, but not in their dependency list for some reason
        "quantstats>=0.0.62",
        "python-dotenv",  # Secret Storage
        "ccxt==4.1.78",
        "termcolor",
        "jsonpickle",
        "apscheduler==3.10.4",
        "appdirs",
        "pyarrow",
        "tqdm",
        "lumiwealth-tradier>=0.1.4",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
