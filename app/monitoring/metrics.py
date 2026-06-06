from prometheus_client import Counter
from prometheus_client import Histogram

REQUEST_COUNT = Counter(
    "farm_inventory_requests_total",
    "Total HTTP Requests",
    ["method", "endpoint"]
)

REQUEST_LATENCY = Histogram(
    "farm_inventory_request_duration_seconds",
    "Request Duration",
    ["method", "endpoint"]
)