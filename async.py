# https://docs.python.org/3/library/asyncio.html
import asyncio
import time

'''
async def main():                             # This is the main function that will run first
    print("This is a async function 1")       # Print a message
    await main2()                             # Wait for main2 to complete before proceeding
    print("Completed after main 2")           # Print a message

async def creating_task():                    # This function creates a task that runs main2 function
    print("This ia a task")                   # Print a message
    task = asyncio.create_task(main2())       # Create a task that runs main2 function
    print("Task created")                     # Print a message
    await task                                # Wait for the task to complete
    print("Task completed")                   # Print a message

async def main2():                            # This function simply waits for 3 seconds before completing
    print("This is a async function 2")       # Print a message
    await asyncio.sleep(3)                    # Wait for 3 seconds

asyncio.run(main())                           # Run the main function
asyncio.run(creating_task())                  # Run the creating_task function
'''

 

import asyncio
import time

def calculate_sequential(in_range, div_by):
    res = []
    for i in range(in_range):
        if i % div_by == 0:
            res.append(i)
    #print(res)        
    return res

async def calculate_concurrent(in_range, div_by):
    res = []
    for i in range(in_range):
        if i % div_by == 0:
            res.append(i)
    #print(res)        
    return res

async def main():
    # Sequential execution
    start_time_sequential = time.time()
    calculate_sequential(500020000, 43)        
    calculate_sequential(50020000, 5)
    calculate_sequential(50020000, 17)
    end_time_sequential = time.time()
    print(f"Sequential execution time: {end_time_sequential - start_time_sequential:.2f} seconds")
    
    # Concurrent execution
    start_time_concurrent = time.time()
    task1 = asyncio.create_task(calculate_concurrent(500020000, 43))
    task2 = asyncio.create_task(calculate_concurrent(50020000, 5))
    task3 = asyncio.create_task(calculate_concurrent(50020000, 17))
    await asyncio.gather(task1, task2, task3)
    end_time_concurrent = time.time()
    print(f"Concurrent execution time: {end_time_concurrent - start_time_concurrent:.2f} seconds")


'''
The output for me is :
Sequential execution time: 16.33 seconds
Concurrent execution time: 15.98 seconds
'''



if __name__ == "__main__":
    asyncio.run(main())
