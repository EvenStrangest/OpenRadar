import setuptools
import codecs

def read_text(filepath):
    with codecs.open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def versionDev():
    from setuptools_scm.version import get_local_dirty_tag
    def clean_scheme(version):
        return get_local_dirty_tag(version) if version.dirty else ''

    return {'local_scheme': clean_scheme}

requirements = read_text(os.path.join(here, 'requirements.txt')).splitlines()

setuptools.setup(
    name="openradar",
    version="1.0.0",
    author="Edwin Pan, Jingning Tang, Dashiell Kosaka, Arjun Gupta, Ruihao Yao",
    author_email="presenseradar@gmail.com",
    description="A mmWave radar data processing library",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    use_scm_version = versionDev,
    setup_requires=['setuptools_scm'],
)
