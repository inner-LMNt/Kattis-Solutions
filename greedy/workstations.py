import heapq

num_researchers, inactivity = map(int, input().split())

researchers = []

for i in range(1, num_researchers + 1):
    arrival, use_time = map(int, input().split())
    researchers.append((arrival, use_time))

# sort by earliest arrival time
researchers.sort(key=lambda x: x[0])

times_unlocked = 1 # first unlock is required

freed = researchers[0][0] + researchers[0][1] # first instance of freed workstation
expire = freed + inactivity # first instance of workstation expiration

# heap to store workstation expiration times
open_workstations = [(freed, expire)] # popped element will be the workstation that was freed earliest

for i in range(1, num_researchers):
    arrival, use_time = researchers[i]

    # Clear expired workstations
    while open_workstations and open_workstations[0][1] < arrival:
        heapq.heappop(open_workstations)

    # If arrival time is between freed and expire, use that workstation
    if open_workstations and open_workstations[0][0] <= arrival <= open_workstations[0][1]:
        freed = arrival + use_time
        expire = freed + inactivity
        heapq.heappop(open_workstations)
        heapq.heappush(open_workstations, (freed, expire))

    # If no workstations are open, use a new workstation
    else:
        freed = arrival + use_time
        expire = freed + inactivity
        heapq.heappush(open_workstations, (freed, expire))
        times_unlocked += 1

print(len(researchers) - times_unlocked)