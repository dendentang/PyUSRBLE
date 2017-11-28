   ## PyUSRBLE
Python interface to USR-BLEXXX series on Linux.

This project provides a simple interface to use USR-BLE series with Python 3 on Linux x86 system. Already tested on raspbianas master side.

   ### Installation
The code needs ```bluepy``` to execute.
```
sudo apt-get install python3-pip libglib2.0-dev
sudo pip3 install bluepy
```

   ### Usage
```from PyUSRBLE import *```

```scanBLE()``` for searching USR-BLE devices(in default setting)

```Uart("aa:bb:cc:dd:ee:ff")``` to initialize

```Uart.read(timeout)``` to read

```Uart.write()``` to write
