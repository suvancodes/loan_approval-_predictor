import os
import logging
from datetime import datetime

# On Vercel, use /tmp (writable) instead of ./logs (read-only)
log_dir = "/tmp/logs" if os.environ.get("VERCEL") else "logs"

# Only try to create logs directory if not on Vercel
if not os.environ.get("VERCEL"):
    os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(log_dir, f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log")

# Create a logger
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)