
import sys
import sentry_sdk

sentry_sdk.init(
    "http://72f1ce49f18445279f6a165779543f0b@localhost:8000/10",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
    release="e6927009298695f8ebf5747eacef4b4ae4963124"
)


def run():
    # Comment for commit
    # New Comment
    val = [1,2,3]
    print(f"{val[4]}") 


if __name__ == '__main__':
    run()
