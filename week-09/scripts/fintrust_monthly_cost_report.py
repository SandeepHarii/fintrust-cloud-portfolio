import boto3
from datetime import date


class FinTrustMonthlyReport:
    def __init__(self, bucket_name):
        self.ce = boto3.client("ce", region_name="us-east-1")
        self.s3 = boto3.client("s3")
        self.bucket_name = bucket_name

    def get_monthly_spend_by_service(self, year, month):
        """
        Returns a dictionary mapping AWS service names
        to their total spend for the given month.
        """

        start = f"{year}-{month:02d}-01"

        if month == 12:
            end = f"{year + 1}-01-01"
        else:
            end = f"{year}-{month + 1:02d}-01"

        response = self.ce.get_cost_and_usage(
            TimePeriod={
                "Start": start,
                "End": end
            },
            Granularity="MONTHLY",
            Metrics=["UnblendedCost"],
            GroupBy=[
                {
                    "Type": "DIMENSION",
                    "Key": "SERVICE"
                }
            ]
        )

        results = {}

        for group in response["ResultsByTime"][0]["Groups"]:
            service = group["Keys"][0]
            cost = float(
                group["Metrics"]["UnblendedCost"]["Amount"]
            )

            if cost > 0.01:
                results[service] = round(cost, 2)

        return results

    def get_last_three_months(self):
        """
        Returns the three most recent calendar months.
        """

        today = date.today()

        months = []

        year = today.year
        month = today.month

        for _ in range(3):
            months.append((year, month))

            month -= 1

            if month == 0:
                month = 12
                year -= 1

        months.reverse()

        return months

    def get_top_five_services(self, monthly_spend):
        """
        Identifies the top five services based on
        average spend across the three months.
        """

        all_services = set()

        for month_data in monthly_spend.values():
            all_services.update(month_data.keys())

        averages = {}

        for service in all_services:
            total = sum(
                monthly_spend[month].get(service, 0)
                for month in monthly_spend
            )

            averages[service] = total / 3

        top_five = sorted(
            averages.items(),
            key=lambda item: item[1],
            reverse=True
        )[:5]

        return [service for service, _ in top_five]

    def calculate_mom_change(self, previous, current):
        """
        Calculates the percentage change from the previous
        month to the current month.
        """

        if previous == 0:
            return None

        return ((current - previous) / previous) * 100

    def build_report(self):
        """
        Builds the monthly FinTrust cost report.
        """

        months = self.get_last_three_months()

        monthly_spend = {}

        for year, month in months:
            month_key = f"{year}-{month:02d}"

            print(f"Querying AWS Cost Explorer for {month_key}...")

            monthly_spend[month_key] = (
                self.get_monthly_spend_by_service(year, month)
            )

        top_five = self.get_top_five_services(monthly_spend)

        month1 = f"{months[0][0]}-{months[0][1]:02d}"
        month2 = f"{months[1][0]}-{months[1][1]:02d}"
        month3 = f"{months[2][0]}-{months[2][1]:02d}"

        report_lines = []

        report_lines.append("FinTrust Monthly AWS Cost Report")
        report_lines.append("=" * 110)
        report_lines.append("")
        report_lines.append(
            f"Reporting Period: {month1} to {month3}"
        )
        report_lines.append(
            "Metric: UnblendedCost"
        )
        report_lines.append("")

        report_lines.append(
            f"{'Service':<40}"
            f"{month1:>15}"
            f"{month2:>15}"
            f"{month3:>15}"
            f"{'MoM Change':>15}"
        )

        report_lines.append("-" * 110)

        for service in top_five:
            cost1 = monthly_spend[month1].get(service, 0)
            cost2 = monthly_spend[month2].get(service, 0)
            cost3 = monthly_spend[month3].get(service, 0)

            mom_change = self.calculate_mom_change(
                cost2,
                cost3
            )

            if mom_change is None:
                mom_display = "N/A"
            elif mom_change >= 0:
                mom_display = f"+{mom_change:.1f}%"
            else:
                mom_display = f"{mom_change:.1f}%"

            service_display = service[:40]

            report_lines.append(
                f"{service_display:<40}"
                f"${cost1:>14,.2f}"
                f"${cost2:>14,.2f}"
                f"${cost3:>14,.2f}"
                f"{mom_display:>15}"
            )

        report_lines.append("-" * 110)
        report_lines.append("")
        report_lines.append(
            "Top 5 services are ranked by average spend across the "
            "three-month reporting period."
        )

        return "\n".join(report_lines)

    def upload_report(self, report_string):
        """
        Uploads the report to the FinTrust S3 cost-report bucket.
        """

        today = date.today()

        key = (
            f"{today.year}-{today.month:02d}/"
            "monthly_summary.txt"
        )

        self.s3.put_object(
            Bucket=self.bucket_name,
            Key=key,
            Body=report_string.encode("utf-8"),
            ContentType="text/plain"
        )

        return key


def main():
    bucket_name = "fintrust-cost-reports"

    report_generator = FinTrustMonthlyReport(
        bucket_name
    )

    report = report_generator.build_report()

    print()
    print(report)

    key = report_generator.upload_report(report)

    print()
    print("Report uploaded successfully.")
    print(f"s3://{bucket_name}/{key}")


if __name__ == "__main__":
    main()