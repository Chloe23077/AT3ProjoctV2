# AT3ProjoctV2
## first update carpark project
![AT3P1](https://github.com/Chloe23077/AT3ProjoctV2/assets/141309342/4db47fa6-76c8-4dae-b0fa-1d7be9402b3b)

### Identify classes, methods, and attributes
| Class Name | Attributes    | Methods                    |
| ---------- | ----------    | ------------------------   |       
| `Carpark`  |name,          |__init__                    |
|            |lacation,      |update_temperature          |
|            |max_bays,      |publicsh_car_status         |
|            |occupied,      |add_car                     |
|            |displays,      |remove_car                  |
|            |bays,          |is_full                     |
|            |cars           |register_display            |
| `Sensor`   |car_park       |__init__                    |
|            |               |_read_plate                 |
|            |               |detect                      |
|            |               |update_car_park             |
| `Display`  |temperature,   |__init__                    |
|            |available_bays,|display_board               |
|            |show_full,     |                            |
|            |banner         |                            |
| `Config`   |file_name      |__init__                    |
|            |config         |                            |
|`test_carpark'|self.car_park|test_carpark_is_instantiated|
|            |               |test_display_is_instantiated|
|            |               |test_sensor_is_instantiated |
|            |               |setUp                       |

![AT3P2](https://github.com/Chloe23077/AT3ProjoctV2/assets/141309342/138ae3e6-e1b8-40c1-90c2-3fbffc03b2af)

![AT3P3](https://github.com/Chloe23077/AT3ProjoctV2/assets/141309342/92ebaf86-cd48-4ad9-aac7-7f1df1d70b2f)

#### Q. Which class is responsible for the number of available bays (and why)? 
##### I think the class resopnsible for the number of available bays is the carpark class. 
##### This is because I think it tracks the current status in the carpark and manages the available bays.
#### Q. Which class is responsible for the current temperature (and why)? 
##### I think the class responsible for the number of available bays is the carpark class.
##### This is because I think is tracks the current status in the carpark and manages the available bays.
#### Q. Which class is responsible for the time (and why)?
##### Like temperature, I think the carpark class manages time. This is because Carpark thinks that the display is updateed and the display class
##### receives and displays the updated information.

![AT3P4](https://github.com/Chloe23077/AT3ProjoctV2/assets/141309342/02b333c1-7d14-4404-9f9e-9b65f9dfdce1)

![AT3P5](https://github.com/Chloe23077/AT3ProjoctV2/assets/141309342/3de7ab2a-c0b1-4c37-bd50-53c85c07ab87)

![AT3P6](https://github.com/Chloe23077/AT3ProjoctV2/assets/141309342/7f5add2d-efee-453a-95f4-571b3ce2d0d6)

![image](https://github.com/Chloe23077/AT3ProjoctV2/assets/141309342/c936d956-203e-4567-91ab-e69c0a6f9bb0)


### Test the car park register method

The car park register method should accept a `Sensor` or `Display` object. It should raise a `TypeError` if the object is neither a `Sensor` nor a `Display`. Before proceeding, think about where you would test this behaviour. Should you test it in the `CarPark` unit tests or the `Sensor` unit tests? Why?

Registering the objects (sensors and displays) in the CarPark class and updating their status seems more appropriate within the context of the CarPark class. This is because the sensors detect the entry and exit of vehicles, notifying the CarPark, which, in turn, updates the displays. Given this flow of interaction, the responsibility for registering and updating lies with the CarPark. Therefore, testing these actions in the unit tests for the CarPark class is deemed suitable.


![AT3P7](https://github.com/Chloe23077/AT3ProjoctV2/assets/141309342/d447be1c-2292-43d5-9f5a-ad77d0761839)

![AT3P8](https://github.com/Chloe23077/AT3ProjoctV2/assets/141309342/6e2baab9-553e-463f-8ab5-7a97cfd30503)

![AT3P9](https://github.com/Chloe23077/AT3ProjoctV2/assets/141309342/b223a81b-9935-4b48-93fd-0a8418510d25)

![AT3P10](https://github.com/Chloe23077/AT3ProjoctV2/assets/141309342/45541893-0b5d-4c34-a968-bb9f7fe421bf)
