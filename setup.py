from distutils.core import setup
setup(
    name='image_processing',
    version='0.0.1',
    description="image processing scripts",
    author="aguiroz",
    install_requires=['Pillow==3.4.2'],
    scripts=['scripts/average.py','scripts/median.py','scripts/prewitt_width.py','scripts/gaussian.py','scripts/prewitt_height.py','scripts/weighted_average.py']
)
