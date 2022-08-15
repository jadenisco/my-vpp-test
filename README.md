# my-vpp-test

## This repository is to be used as a simple attempt at setting up a vpp test infrastructure

### VPP API

To run a test we will need a working version of the VPP API. These test will assume a running VPP and valid VPP API.

We also assume there a valid VPP running.

#### Install the Python virtual environment package

``` console
$ sudo apt-get install python3-pip
$ sudo pip3 install virtualenv

```

## Install the virtual environment for this app

I did this from the VSCode terminal. With VSCode after you create the environment you should be asked if you want to use this environment. Say yes.

``` console
$ python3 -m venv .venv

```

## Build and install the vpp python api

``` console
$ export VPP="Some VPP root directory"
$ pushd $VPP/src/vpp-api/python/
$ python setup.py install
$ popd
```

## LD_LIBRARY_PATH

The LD_LIBRARY_PATH is set in the vpp_api_hello.py program. LD_LIBRARY_PATH needs to point to libvppapiclient.so. If VPP is installed LD_LIBRARY_PATH should point to '/usr/lib/x86_64-linux-gnu/'.

