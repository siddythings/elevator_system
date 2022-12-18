# Problem Statement

## API’s required:
### Initialise the elevator system to create ‘n’ elevators in the system
```
curl --location --request POST 'localhost:8000/api/elevator-system/initialize/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "num_elevators": 0
}'
```

### Fetch all requests for a given elevator
```
curl --location --request GET 'localhost:8000/api/elevators/1/requests/'
```

### Fetch the next destination floor for a given elevator
```
curl --location --request POST 'localhost:8000/api/elevators/1/requests/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "floor": 5
}'
```
Responce
```
{
    "status": true,
    "message": "Elevator",
    "data": {
        "id": 6,
        "floor": 5,
        "direction": "",
        "updated_at": "2022-12-18T07:54:01.948344Z",
        "created_at": "2022-12-18T07:54:01.948378Z",
        "is_checked": false,
        "elevator": 1
    }
}
```

### Fetch if the elevator is moving up or down currently
```
curl --location --request POST 'localhost:8000/api/elevators/1/next-destination/'
```
Responce
```
{
    "status": true,
    "message": "Elevator",
    "data": {
        "id": 5,
        "floor": 5,
        "direction": "up",
        "updated_at": "2022-12-18T07:53:23.593347Z",
        "created_at": "2022-12-18T07:53:23.593619Z",
        "is_checked": false,
        "elevator": 1,
        "distination": false,
        "current_floor": 1
    }
}
```
### Saves user request to the list of requests for a elevator
```
curl --location --request GET 'localhost:8000/api/elevators/1/requests/'
```

### Mark a elevator as not working or in maintenance 
Incase of OnMaintenance
```
curl --location --request POST 'localhost:8000/api/elevators-maintenance/1/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "status":false,
    "reason":"due to water"
}'
```
Incase of Available
```
curl --location --request POST 'localhost:8000/api/elevators-maintenance/1/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "status":true,
    "reason":"due to water"
}'
```
Responce
```
{
    "status": true,
    "message": "Elevator",
    "data": {
        "status": true,
        "reason": "due to water"
    }
}
```

### Open/close the door.

```
curl --location --request POST 'localhost:8000/api/elevators/1/next-destination/'
```

### Things we can do more
1: Elevators failure System
2: Elevator Emergency Alarm
3: Elevator Restart System After failure