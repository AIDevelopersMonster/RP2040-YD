# SPDX-FileCopyrightText: Copyright (c) 2022 Makerdiary
#
# SPDX-License-Identifier: MIT

"""
`ltr381rgb`
================================================================================
Python LTR381RGB optical sensor library
* Author(s): Makerdiary
Implementation Notes
--------------------
**Software and Dependencies:**
* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads
* Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
* Adafruit's Register library: https://github.com/adafruit/Adafruit_CircuitPython_Register
"""

import time
from micropython import const
from adafruit_bus_device import i2c_device
from adafruit_register.i2c_struct import ROUnaryStruct
from adafruit_register.i2c_bits import RWBits
from adafruit_register.i2c_bit import RWBit, ROBit

try:
    from typing import Tuple
    from busio import I2C
except ImportError:
    pass

_LTR381RGB_I2CADDR_DEFAULT: int = const(0x53)  # Default I2C address
_LTR381RGB_PART_ID_DEFAULT = const(0xC2)

_LTR381RGB_MAIN_CTRL = const(0x00)
_LTR381RGB_ALS_CS_MEAS_RATE = const(0x04)
_LTR381RGB_ALS_CS_GAIN = const(0x05)
_LTR381RGB_PART_ID = const(0x06)
_LTR381RGB_MAIN_STATUS = const(0x07)
_LTR381RGB_CS_DATA_IR_0 = const(0x0A)
_LTR381RGB_CS_DATA_GREEN_0 = const(0x0D)
_LTR381RGB_CS_DATA_RED_0 = const(0x10)
_LTR381RGB_CS_DATA_BLUE_0 = const(0x13)
_LTR381RGB_INT_CFG = const(0x19)
_LTR381RGB_INT_PST = const(0x1A)
_LTR381RGB_ALS_THRES_UP_0 = const(0x21)
_LTR381RGB_ALS_THRES_LOW_0 = const(0x24)

MODE_ALS = "ALS"
MODE_CS = "CS"

_LTR381RGB_MODES = (MODE_ALS, MODE_CS)

RESOLUTION_20_BIT = "20_BIT"
RESOLUTION_19_BIT = "19_BIT"
RESOLUTION_18_BIT = "18_BIT"
RESOLUTION_17_BIT = "17_BIT"
RESOLUTION_16_BIT = "16_BIT"

_LTR381RGB_RESOLUTIONS = (
    RESOLUTION_20_BIT,
    RESOLUTION_19_BIT,
    RESOLUTION_18_BIT,
    RESOLUTION_17_BIT,
    RESOLUTION_16_BIT,
)

_LTR381RGB_RESOLUTIONS_INT = (
    (RESOLUTION_20_BIT, 0, 0.25),
    (RESOLUTION_19_BIT, 1, 0.5),
    (RESOLUTION_18_BIT, 2, 1),
    (RESOLUTION_17_BIT, 3, 2),
    (RESOLUTION_16_BIT, 4, 4),
)

RATE_25_MS = "25_MS"
RATE_50_MS = "50_MS"
RATE_100_MS = "100_MS"
RATE_200_MS = "200_MS"
RATE_500_MS = "500_MS"
RATE_1000_MS = "1000_MS"
RATE_2000_MS = "2000_MS"

_LTR381RGB_RATES = (
    RATE_25_MS,
    RATE_50_MS,
    RATE_100_MS,
    RATE_200_MS,
    RATE_500_MS,
    RATE_1000_MS,
    RATE_2000_MS,
)

_LTR381RGB_RATES_MS = (
    (RATE_25_MS, 0, 25),
    (RATE_50_MS, 1, 50),
    (RATE_100_MS, 2, 100),
    (RATE_200_MS, 3, 200),
    (RATE_500_MS, 4, 500),
    (RATE_1000_MS, 5, 1000),
    (RATE_2000_MS, 6, 2000),
)

GAIN_X1 = 1
GAIN_X3 = 3
GAIN_X6 = 6
GAIN_X9 = 9
GAIN_X18 = 18

_LTR381RGB_GAINS = (
    GAIN_X1,
    GAIN_X3,
    GAIN_X6,
    GAIN_X9,
    GAIN_X18,
)

_LTR381RGB_GAINS_RANGE = (
    (GAIN_X1, 0),
    (GAIN_X3, 1),
    (GAIN_X6, 2),
    (GAIN_X9, 3),
    (GAIN_X18, 4),
)

class LTR381RGB:
    """Driver for the LTR381RGB optical sensor.
    **Quickstart: Importing and using the device**
    Here is an example of using the :py:class:`MMC5603` class.
    First you will need to import the libraries to use the sensor
    .. code-block:: python
        import board
        from ltr381rgb import LTR381RGB
    Once this is done you can define your `board.I2C` object and define your sensor object
    .. code-block:: python
        i2c = board.I2C()
        sensor = LTR381RGB(i2c)
    Now you have access to the :attr:`lux` attribute
    .. code-block:: python
        lux = sensor.lux
    :param ~busio.I2C i2c_bus: The I2C bus the LTR381RGB is connected to.
    :param int address: The I2C device address. Defaults to :const:`0x53`
    """

    _part_id = ROUnaryStruct(_LTR381RGB_PART_ID, "<B")

    _als_cs_enable = RWBit(_LTR381RGB_MAIN_CTRL, 1)
    _cs_mode = RWBit(_LTR381RGB_MAIN_CTRL, 2)
    _als_cs_resolution = RWBits(3, _LTR381RGB_ALS_CS_MEAS_RATE, 4)
    _als_cs_meas_rate = RWBits(3, _LTR381RGB_ALS_CS_MEAS_RATE, 0)
    _als_cs_gain_range = RWBits(3, _LTR381RGB_ALS_CS_GAIN, 0)
    _als_cs_data_status = ROBit(_LTR381RGB_MAIN_STATUS, 3)

    def __init__(self, i2c_bus: I2C, address: int = _LTR381RGB_I2CADDR_DEFAULT, wfac: float = 1.0) -> None:
        # pylint: disable=no-member
        self.i2c_device = i2c_device.I2CDevice(i2c_bus, address)
        if self._part_id != _LTR381RGB_PART_ID_DEFAULT:
            raise RuntimeError("Failed to find LTR381RGB - check your wiring!")
        self._mode = MODE_ALS
        self._resolution = RESOLUTION_18_BIT
        self._integration_time = 1
        self._rate = RATE_100_MS
        self._gain = GAIN_X3
        self._wfac = wfac
        self._buffer = bytearray(12)

    def enable(self) -> None:
        """Set the sensor to active mode"""
        self._als_cs_enable = 1
        time.sleep(0.01)

    def disable(self) -> None:
        """Set the sensor to standby mode"""
        self._als_cs_enable = 0

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        if not value in _LTR381RGB_MODES:
            raise ValueError("Mode '%s' not supported" % (value))
        if not self._mode == value:
            if value == MODE_ALS:
                self._cs_mode = 0
            else:
                self._cs_mode = 1
            self._mode = value

    @property
    def resolution(self):
        """
        ALS/CS Resolution/Bit Width
        Allowed values are the constants RESOLUTION_*
        """
        return self._resolution

    @resolution.setter
    def resolution(self, value):
        if not value in _LTR381RGB_RESOLUTIONS:
            raise ValueError(
                "ALS/CS resolution '%s' not supported" % (value)
            )
        if not self._resolution == value:
            for res_int in _LTR381RGB_RESOLUTIONS_INT:
                if value == res_int[0]:
                    self._als_cs_resolution = res_int[1]
                    self._resolution = value
                    self._integration_time = res_int[2]
                    break

    @property
    def rate(self):
        """
        ALS/CS Measurement Rate
        Allowed values are the constants RESOLUTION_*
        """
        return self._rate

    @rate.setter
    def rate(self, value):
        if not value in _LTR381RGB_RATES:
            raise ValueError(
                "ALS/CS Measurement Rate '%s' not supported" % (value)
            )
        if not self._rate == value:
            for rate_ms in _LTR381RGB_RATES_MS:
                if value == rate_ms[0]:
                    self._als_cs_meas_rate = rate_ms[1]
                    self._rate = value
                    break

    @property
    def gain(self):
        """
        ALS/CS measurement Gain Range
        Allowed values are the constants GAIN_*
        """
        return self._gain

    @gain.setter
    def gain(self, value):
        if not value in _LTR381RGB_GAINS:
            raise ValueError(
                "ALS/CS measurement Gain Range '%s' not supported" % (value)
            )
        if not self._gain == value:
            for g in _LTR381RGB_GAINS_RANGE:
                if value == g[0]:
                    self._als_cs_gain_range = g[1]
                    self._gain = value
                    break

    @property
    def is_data_new(self) -> bool:
        return bool(self._als_cs_data_status)
    
    @property
    def raw_data(self) -> tuple[int, int, int, int]:

        self._buffer[0] = _LTR381RGB_CS_DATA_IR_0
        with self.i2c_device as i2c:
            i2c.write_then_readinto(self._buffer, self._buffer, out_end=1)
        
        ir = self._buffer[2] << 16 | self._buffer[1] << 8 | self._buffer[0]
        g = self._buffer[5] << 16 | self._buffer[4] << 8 | self._buffer[3]
        r = self._buffer[8] << 16 | self._buffer[7] << 8 | self._buffer[6]
        b = self._buffer[11] << 16 | self._buffer[10] << 8 | self._buffer[9]

        return (ir, g, r, b)

    @property
    def lux(self) -> float:
        ir, g, r, b = self.raw_data
        return 0.8 * g / (self._gain * self._integration_time) * (1 - 0.033 * ir / g) * self._wfac
