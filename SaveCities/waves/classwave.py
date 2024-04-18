import asyncio

initial_speed = 1.0
maximum_speed = 0.1
speed_increment = 0.1
change_interval = 5 

async def dynamic_speed_task(task_number):
    current_speed = initial_speed
    last_change_time = asyncio.get_event_loop().time()

    while current_speed > maximum_speed:
        print(f"Task {task_number} is being executed at a speed of: {current_speed} seconds between iterations.")
        
        if asyncio.get_event_loop().time() - last_change_time >= change_interval:
            current_speed = max(current_speed - speed_increment, maximum_speed)
            print(f"Speed for Task {task_number} changed. New speed: {current_speed}.")
            last_change_time = asyncio.get_event_loop().time()
        
        await asyncio.sleep(current_speed)

async def main():
    await asyncio.gather(
        dynamic_speed_task(1),
        dynamic_speed_task(2),
        dynamic_speed_task(3)
    )

asyncio.run(main())
