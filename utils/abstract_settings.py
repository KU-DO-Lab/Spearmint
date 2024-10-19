from abc import ABC, abstractmethod
from typing import Dict, Any, List, Callable, Optional
from dataclasses import dataclass, field

class BaseSweepSettings(ABC):
    '''Base class for instrument settings.

    It is a bit tedious to set the settings for each measurement as they differ in their implementations a bit. We can rigidly define the settings here and create implementations for each measurement.

    '''
    @abstractmethod
    def set(self, **kwargs):
        pass

    @abstractmethod
    def get(self) -> Dict[str, Any]:
        pass

@dataclass
class SweepParam:
    start: float
    stop: float
    step: float

@dataclass
class Sweep1DSettings(BaseSweepSettings):
    params: SweepParam = field(default_factory=lambda: SweepParam(0.0, 0.0, 0.0))
    step_sec: float = 0.0
    continual: bool = False
    bidirectional: bool = False 
    plot_bin: int = 1
    save_data: bool = True 
    plot_data: bool = True 
    ramp_to_start: bool = True

    def set(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

            
    def get(self) -> Dict[str, Any]:
        return {
            'start': self.params.start,
            'stop': self.params.stop,
            'step': self.params.step,
            'step_sec': self.step_sec,
            'bidirectional': self.bidirectional,
            'plot_bin': self.plot_bin,
            'save_data': self.save_data,
            'plot_data': self.plot_data,
            'ramp_to_start': self.ramp_to_start
        }
