import os
import sys
import sentry_sdk

import sentry_sdk

sentry_sdk.init(
    dsn="https://1c5d784f7ad85c0ce3684ae39f352bf8@o4506186993238016.ingest.sentry.io/4506198600450048",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

def run():
    # Comment for commit
    # New Comment
    val = [1,2,3]
    print(f"{val[2]}") 


if __name__ == '__main__':
    run()
