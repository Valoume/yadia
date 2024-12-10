import os
from app import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # Try alternative ports if the default port is in use
    max_attempts = 3
    for attempt in range(max_attempts):
        try:
            app.run(host="0.0.0.0", port=port, debug=True)
            break
        except OSError as e:
            if "Address already in use" in str(e) and attempt < max_attempts - 1:
                port += 1
                continue
            raise e
