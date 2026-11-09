
import dns.resolver
import argparse


RECORD_TYPES = ["A", "AAAA", "MX", "NS", "CNAME", "TXT"]


def lookup_record(domain, record_type):
    print(f"\n[{record_type} Records]")

    try:
        answers = dns.resolver.resolve(domain, record_type)

        for answer in answers:
            print(f"  {answer}")

    except dns.resolver.NoAnswer:
        print("  No records found.")

    except dns.resolver.NXDOMAIN:
        print("  Domain does not exist.")

    except dns.resolver.NoNameservers:
        print("  No responsive DNS nameservers.")

    except dns.resolver.Timeout:
        print("  DNS query timed out.")

    except Exception as error:
        print(f"  Error: {error}")


def analyze_domain(domain):
    print("=" * 50)
    print("           DNS LOOKUP ANALYZER")
    print("=" * 50)

    print(f"Target Domain: {domain}")

    for record_type in RECORD_TYPES:
        lookup_record(domain, record_type)

    print("\n" + "=" * 50)
    print("DNS Analysis Completed.")
    print("=" * 50)


def main():
    parser = argparse.ArgumentParser(
        description="Python DNS Lookup and Analyzer"
    )

    parser.add_argument(
        "domain",
        help="Domain name to investigate"
    )

    args = parser.parse_args()

    analyze_domain(args.domain)


if __name__ == "__main__":
    main()
