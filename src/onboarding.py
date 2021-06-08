
import sys
import sentry_sdk

sentry_sdk.init(
    "https://e03c8dc2af3d45bdb0106009c59d30d3@o815923.ingest.sentry.io/5807218",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)


def run():
    if len(sys.argv >= 2 and int(sys.argv[2]) != 0):
        value = int(sys.argv[1]) / int(sys.argv[2])
        print(f"Value is {value}")


if __name__ == '__main__':
    run()
