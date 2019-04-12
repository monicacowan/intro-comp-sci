# This program calculates the total time spent at routers between
# Birmingham, England and Sundsvall, Sweden.

traceroute_ms = 75.0 # ms, round trip.
distance_km = 2500.0 # km, one-way
data_speed_kmps = 200000.0 #km/s

travel_time = distance_km * 2 * 1000 / data_speed_kmps # ms, round trip

router_time = traceroute_ms - travel_time

print 'router time is ', router_time
print 'travel time was ', travel_time
