-- Active: 1677827838126@@localhost@3306@mysql
INSERT INTO `mysql`.`drone_type` 
(id, engine_power, flight_range, load_capacity, cargo_volume, battery_capacity) 
VALUES (1, 500, 200, 800, 20, 100);

INSERT INTO `mysql`.`drone`
(id, access_key, drone_status, place_number, id_drone_type)
VALUES (1, "123qwe", "READY", 1, 1);

INSERT INTO `mysql`.`cargo`
(id, weight, volume, name)
VALUES (1, 100, 10, "box");

INSERT INTO `mysql`.`task`
(id, created_at, gps_latitude, gps_longitude, priority, task_status, id_drone, id_cargo)
VALUES (1, "2023-03-03 13:28:14", 50.5, 60.6, "VIP", "NEW", 1, 1); 

INSERT INTO `mysql`.`task`
(id, created_at, gps_latitude, gps_longitude, priority, task_status, id_drone, id_cargo)
VALUES (2, "2023-03-03 13:28:14", 50.5, 60.6, "VIP", "NEW", 1, 1);

INSERT INTO `mysql`.`charging_point`
(id, power)
VALUES (1, 100);

INSERT INTO `mysql`.`charging_point_to_drone`
(charging_point_id, drone_id, id)
VALUES (1, 1, 1); 

INSERT INTO `mysql`.`drone_type`
(id, engine_power, flight_range, load_capacity, cargo_volume, battery_capacity)
VALUES (2, 1000, 400, 1600, 40, 200); 

INSERT INTO `mysql`.`drone_type`
(id, engine_power, flight_range, load_capacity, cargo_volume, battery_capacity)
VALUES (3, 1500, 600, 2400, 60, 300);

SELECT 
drone_type.id, drone_type.engine_power, drone_type.flight_range, 
drone_type.load_capacity, drone_type.cargo_volume, drone_type.battery_capacity 
FROM drone_type WHERE drone_type.id = 1;

INSERT INTO `mysql`.`cargo`
(id, weight, volume, name)
VALUES (3, 100, 10, "Computer");

INSERT INTO `mysql`.`task`
(id, created_at, gps_latitude, gps_longitude, priority, task_status, id_cargo)
VALUES (4, "2023-03-03 13:28:14", 55.108175, 37.975712, NULL, "NEW", 3); 

SELECT * FROM `mysql`.`task` WHERE task_status = "NEW";