import os
import sys
import sentry_sdk

sentry_sdk.init(
    dsn="https://fc6c674a719249f4abc7c8499de2747d@o815923.ingest.sentry.io/4505478865551360",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)


def run():
    # Comment for commit
    # New Comment
    val = [1,2,3]
    print(f"{val[4]}") 


if __name__ == '__main__':
    run()
