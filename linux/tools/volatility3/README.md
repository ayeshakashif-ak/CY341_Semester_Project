# Volatility 3: The volatile memory extraction framework

Volatility is the world's most widely used framework for extracting digital
artifacts from volatile memory (RAM) samples. The extraction techniques are
performed completely independent of the system being investigated but offer
visibility into the runtime state of the system. The framework is intended
to introduce people to the techniques and complexities associated with
extracting digital artifacts from volatile memory samples and provide a
platform for further work into this exciting area of research.

In 2019, the Volatility Foundation released a complete rewrite of the
framework, Volatility 3. The project was intended to address many of the
technical and performance challenges associated with the original
code base that became apparent over the previous 10 years. Another benefit
of the rewrite is that Volatility 3 could be released under a custom
license that was more aligned with the goals of the Volatility community,
the Volatility Software License (VSL). See the
[LICENSE](https://www.volatilityfoundation.org/license/vsl-v1.0) file for
more details.

## Quick Start

1. Install the required dependencies:

    ```shell
    pip install --user -e ".[full]"
    ```

2. See available options:

    ```shell
    vol -h
    ```

3. To get more information on a Windows memory sample and to make sure Volatility supports that sample type, run `vol -f <imagepath> windows.info`:

    ```shell
    vol -f /home/user/samples/stuxnet.vmem windows.info
    ```

4. Run some other plugins. The `-f` or `--single-location` is not strictly required, but most plugins expect a single sample.
Some also require/accept other options.  Run `vol <plugin> -h` for more information on a particular command.

## Installing

Volatility 3 requires Python 3.8.0 or later and is published on the [PyPi registry](https://pypi.org/project/volatility3).

```shell
pip install volatility3
```

If you want to use the latest development version of Volatility 3 we recommend you manually clone this repository and install an editable version of the project.
We recommend you use a virtual environment to keep installed dependencies separate from system packages.

The latest stable version of Volatility will always be the `stable` branch of the GitHub repository. The default branch is `develop`.

```shell
git clone https://github.com/volatilityfoundation/volatility3.git
cd volatility3/
python3 -m venv venv && . venv/bin/activate
pip install -e ".[dev]"
```

## Symbol Tables

Symbol table packs for the various operating systems are available for download at:

<https://downloads.volatilityfoundation.org/volatility3/symbols/windows.zip>
<https://downloads.volatilityfoundation.org/volatility3/symbols/mac.zip>
<https://downloads.volatilityfoundation.org/volatility3/symbols/linux.zip>

The hashes to verify whether any of the symbol pack files have downloaded successfully or have changed can be found at:

<https://downloads.volatilityfoundation.org/volatility3/symbols/SHA256SUMS>
<https://downloads.volatilityfoundation.org/volatility3/symbols/SHA1SUMS>
<https://downloads.volatilityfoundation.org/volatility3/symbols/MD5SUMS>

Symbol tables zip files must be placed, as named, into the `volatility3/symbols` directory (or just the symbols directory next to the executable file).

Windows symbols that cannot be found will be queried, downloaded, generated and cached.  Mac and Linux symbol tables must be manually produced by a tool such as [dwarf2json](https://github.com/volatilityfoundation/dwarf2json).

Important: The first run of volatility with new symbol files will require the cache to be updated.  The symbol packs contain a large number of symbol files and so may take some time to update!
However, this process only needs to be run once on each new symbol file, so assuming the pack stays in the same location will not need to be done again.  Please also note it can be interrupted and next run will restart itself.

Please note: These are representative and are complete up to the point of creation for Windows and Mac.  Due to the ease of compiling Linux kernels and the inability to uniquely distinguish them, an exhaustive set of Linux symbol tables cannot easily be supplied.

## Documentation

The framework is documented through doc strings and can be built using sphinx.

The latest generated copy of the documentation can be found at: <https://volatility3.readthedocs.io/en/latest/>

## Licensing and Copyright

Copyright (C) 2007-2025 Volatility Foundation

All Rights Reserved

<https://www.volatilityfoundation.org/license/vsl-v1.0>

## Bugs and Support

If you think you've found a bug, please report it at:

<https://github.com/volatilityfoundation/volatility3/issues>

In order to help us solve your issues as quickly as possible,
please include the following information when filing a bug:

- The version of Volatility you're using
- The operating system used to run Volatility
- The version of Python used to run Volatility
- The suspected operating system of the memory sample
- The complete command line you used to run Volatility

For community support, please join us on Slack:

<https://www.volatilityfoundation.org/slack>

## Contact

For information or requests, contact:

Volatility Foundation

Web: <https://www.volatilityfoundation.org>

Blog:     <https://volatility-labs.blogspot.com>

Email: volatility (at) volatilityfoundation (dot) org

Twitter: [@volatility](https://twitter.com/volatility)
