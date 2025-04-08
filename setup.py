from setuptools import setup, find_packages

setup(
    name="otlp-package",
    version="1.0.0",
    author="Sravani",
    author_email="sravs8294@gmail.com",
    description="A Python package that is used for tracing",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/21A91A05F5/otlp_package",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "opentelemetry-sdk",         # Includes core OpenTelemetry SDK packages
        "opentelemetry-api",         # Includes OpenTelemetry API packages
        "opentelemetry-exporter-otlp", # For OTLP exporters (both HTTP and GRPC)
        "requests", 
    ],  # List dependencies here if needed
    include_package_data=True,
)
