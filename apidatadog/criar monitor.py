from datadog import initialize, api

options = {
    'api_key': 'xxxxxxxxxxx',
    'app_key': 'xxxxxxxxxxx'
}

initialize(**options)

# Create a new monitor
monitor_options = {
    "notify_no_data": True,
    "no_data_timeframe": 20
}

api.Monitor.create(
    type="query alert",
    query="avg(last_5m):sum:system.mem.free{host:host0} > 10",
    name="Memoria",
    message="está alertando.",
    options=monitor_options
)
