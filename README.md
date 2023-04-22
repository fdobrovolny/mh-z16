# mh-zxx
Lightweight python library for interactions with MH-Z16, MH-Z19 and similar Intelligent Infrared Gas Module CO2

# MH-ZXX CO2 Sensor API

* [CO2Sensor](#mh_zxx.base.CO2Sensor)
  * [\_\_init\_\_](#mh_zxx.base.CO2Sensor.__init__)
  * [read\_co2](#mh_zxx.base.CO2Sensor.read_co2)
  * [read\_temperature](#mh_zxx.base.CO2Sensor.read_temperature)
  * [read\_status](#mh_zxx.base.CO2Sensor.read_status)
  * [read](#mh_zxx.base.CO2Sensor.read)
  * [zero\_calibration](#mh_zxx.base.CO2Sensor.zero_calibration)
  * [span\_calibration](#mh_zxx.base.CO2Sensor.span_calibration)
  * [set\_auto\_calibration](#mh_zxx.base.CO2Sensor.set_auto_calibration)
  * [close](#mh_zxx.base.CO2Sensor.close)

<a id="mh_zxx.base.CO2Sensor"></a>

## CO2Sensor

```python
class CO2Sensor()
```

MH-Z16 and MH-Z19 CO2 sensor.

<a id="mh_zxx.base.CO2Sensor.__init__"></a>

#### \_\_init\_\_

```python
def __init__(port: str, baudrate: int = 9600, timeout: float = 0.2)
```

Setup CO2 sensor

**Arguments**:

- `port`: The serial port name, for example `/dev/ttyUSB0` (Linux),
`/dev/tty.usbserial` (OS X) or `COM4` (Windows).
- `baudrate`: Baudrate to use.
- `timeout`: Read timeout after each command.

<a id="mh_zxx.base.CO2Sensor.read_co2"></a>

#### read\_co2

```python
def read_co2() -> int
```

Read CO2 concentration.

<a id="mh_zxx.base.CO2Sensor.read_temperature"></a>

#### read\_temperature

```python
def read_temperature() -> float
```

Read temperature.

<a id="mh_zxx.base.CO2Sensor.read_status"></a>

#### read\_status

```python
def read_status() -> int
```

Read status.

<a id="mh_zxx.base.CO2Sensor.read"></a>

#### read

```python
def read() -> Tuple[int, float, int, int]
```

Read all values.

**Returns**:

CO2 concentration, temperature, status, co2 auto calibration point

<a id="mh_zxx.base.CO2Sensor.zero_calibration"></a>

#### zero\_calibration

```python
def zero_calibration()
```

Zero calibration.

<a id="mh_zxx.base.CO2Sensor.span_calibration"></a>

#### span\_calibration

```python
def span_calibration(span: int)
```

Span calibration.

<a id="mh_zxx.base.CO2Sensor.set_auto_calibration"></a>

#### set\_auto\_calibration

```python
def set_auto_calibration(state: bool)
```

Set auto calibration point.

<a id="mh_zxx.base.CO2Sensor.close"></a>

#### close

```python
def close()
```

Close serial port.

