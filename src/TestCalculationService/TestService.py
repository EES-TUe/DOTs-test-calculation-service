# -*- coding: utf-8 -*-
from datetime import datetime
import helics as h
from dots_infrastructure.DataClasses import EsdlId, HelicsCalculationInformation, PublicationDescription, TimeStepInformation, TimeRequestType
from dots_infrastructure.HelicsFederateHelpers import HelicsSimulationExecutor
from dots_infrastructure.Logger import LOGGER
from esdl import EnergySystem

class CalculationServiceEConnection(HelicsSimulationExecutor):

    def __init__(self):
        super().__init__()

        publication_values = [
            PublicationDescription(global_flag=True, 
                                   esdl_type="EConnection", 
                                   output_name="EConnectionDispatch", 
                                   output_unit="W", 
                                   data_type=h.HelicsDataType.DOUBLE)
        ]

        e_connection_period_in_seconds = 60

        calculation_information = HelicsCalculationInformation(
            time_period_in_seconds=e_connection_period_in_seconds,
            offset=0, 
            uninterruptible=False, 
            wait_for_current_time_update=False, 
            terminate_on_error=True, 
            calculation_name="EConnectionDispatch", 
            inputs=[], 
            outputs=publication_values, 
            calculation_function=self.e_connection_dispatch
        )
        self.add_calculation(calculation_information)

    def e_connection_dispatch(self, param_dict : dict, simulation_time : datetime, time_step_number : TimeStepInformation, esdl_id : EsdlId, energy_system : EnergySystem):
        raise Exception("Test Exception")

if __name__ == "__main__":

    helics_simulation_executor = CalculationServiceEConnection()
    helics_simulation_executor.start_simulation()
    helics_simulation_executor.stop_simulation()
