from typing import List, Optional, Dict, Any
from pydantic import BaseModel

class RawData(BaseModel):
    adc: Optional[int] = None
    voltage_v: Optional[float] = None
    temp_c: Optional[float] = None
    slope_mV_per_pH: Optional[float] = None
    rom: Optional[str] = None
    resolution_bits: Optional[int] = None
    ec_uS_cm: Optional[float] = None
    salinity_ppt: Optional[float] = None

class Measurement(BaseModel):
    parameter: str
    value: float
    unit: str
    method: str
    temp_compensated: Optional[bool] = None
    uncertainty: Optional[float] = None
    calibration_id: Optional[str] = None
    raw: Optional[RawData]

class Power(BaseModel):
    battery_v: float
    usb_power: bool

class Firmware(BaseModel):
    app: str
    ver: str

class Telemetry(BaseModel):
    version: str
    msg_type: str
    device_id: str
    site_id: str
    sent_at: str
    seq: int
    measurements: List[Measurement]
    power: Power
    rssi_dbm: int
    fw: Firmware
