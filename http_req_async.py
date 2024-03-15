import asyncio                                                  # Import the asyncio module for asynchronous I/O operations.
import aiohttp                                                  # Import the aiohttp module for making asynchronous HTTP requests.
import time                                                     # Import the time module to measure execution time.

async def fetch(session, url):
    try:
        async with session.get(url) as response:                # Make an asynchronous GET request to the URL.
            return await response.text()                           
    except (aiohttp.ClientError, asyncio.TimeoutError) as e:
        print(f"Error fetching {url}: {e}")
        return None                                             # Return None or an appropriate value to indicate failure
    
    
async def main():                                               # Define the main asynchronous function.
    start_time = time.time()                                    # Record the start time of the program.
    urls = [
        'http://example.com',
        'http://example.org',
        'http://example.net',
        'http://example.com/robots.txt',
        'http://example.org/robots.txt',
        'http://example.net/robots.txt',
        'http://example.com/favicon.ico',
        'http://example.org/favicon.ico',
        'http://example.net/favicon.ico',
        'http://example.com/index.html',
        'http://example.org/index.html',
        'http://example.net/index.html',
        'http://example.com/about.html',
        'http://example.org/about.html',
        'http://example.net/about.html',
        'http://example.com/contact.html',
        'http://example.org/contact.html',
        'http://example.net/contact.html',
        'http://example.com/services.html',
        'http://example.org/services.html',
        'http://example.net/services.html',
    ]
    
    async with aiohttp.ClientSession() as session:              # Create an aiohttp client session.
        tasks = []                                              # Initialize an empty list to store the tasks.
        
        for _ in range(100):                                    # Loop 100 times to repeat the fetching process.
            for url in urls:                                    # Iterate over each URL in the list.
                tasks.append(fetch(session, url))               # Append a task to fetch the URL.
        
                                                                # Wait for all tasks to complete.
        responses = await asyncio.gather(*tasks)                # Use asyncio.gather to await all tasks.
        
                                                                # Process responses.
        for response in responses:                              # Iterate over each response.
            print(response[:100])                               # Print the first 100 characters of each response.
            
    end_time = time.time()                                      # Record the end time of the program.
    total_time = end_time - start_time                          # Calculate the total execution time.
    print("Time taken: ", total_time)                           # Print the total execution time.
    
if __name__ == "__main__":
    asyncio.run(main())                                         # Run the main function if the script is executed directly.
