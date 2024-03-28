from setuptools import setup, find_packages


setup(
    name='comments_wagtail_xtd',
    author='Alexander Smolenskyi',
    license='GPLv3',
    author_email='alexsmolenskyi@gmail.com',
    version='1.0.5',
    url='https://github.com/AlexDeltax/wagtail_comments_xtd',
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Topic :: Internet :: WWW/HTTP',
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.10',
    install_requires=[
        "wagtail>=6.0.0",
        "Django>=5.0.0",
        "django-comments-xtd>=2.9.13"
    ],
)
