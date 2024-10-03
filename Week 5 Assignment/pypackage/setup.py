from setuptools import setup, find_packages

setup(
    name="shristi's_project",  # Replace with your project's name
    version='0.1',  # Initial release version
    description='A simple math package',
    long_description=open('README.md').read(),  # If you have a README.md file
    long_description_content_type='text/markdown',  # Type of the long description
    author='Shristi',  # Replace with your name
    author_email='shristi35dahal@gmail.com',  # Replace with your email
    url='https://github.com/your_username/your_project',  # URL to your project
    packages=find_packages(),  # Automatically find the package directory
    include_package_data=True,  # Include non-code files specified in MANIFEST.in
    install_requires=[
        # List of dependencies (libraries) your project needs
        'numpy>=1.18.0',
        'pandas>=1.0.0',
        'tensorflow>=2.0.0',
        # Add more dependencies as required
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify Python version compatibility
    entry_points={
        'console_scripts': [
            'your_command=your_module:main_function',  # Command-line entry points
        ],
    },
)