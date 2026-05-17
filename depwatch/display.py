from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

def show_results(results):
    table = Table(box=box.MINIMAL, show_header=True, show_lines=True)
    table.add_column("TYPE")
    table.add_column("PACKAGE", style="bold")
    table.add_column("CURRENT")
    table.add_column("LATEST")
    table.add_column("STATUS")
    table.add_column("CVE")

    kritik = 0
    guncelleme = 0

    for r in results:
        eko = r.get("ecosystem", "PyPI")
        name = r["name"]
        current = r["version"] or "?"
        latest = r["latest"] or "?"
        vulns = r["vulns"]

        if vulns:
            kritik += 1
            durum = "[bold red]Critical[/bold red]"
            cve_str = "\n".join([
                v['cve'] or v['id'] for v in vulns
            ])
        elif current != latest and current != "?":
            guncelleme += 1
            durum = "Outdated"
            cve_str = "-"
        else:
            durum = "Up to date"
            cve_str = "-"

        table.add_row(eko, name, current, latest, durum, cve_str)

    console.print("\nDEPWATCH RESULTS\n")
    console.print(table)
    console.print(
        f"\nSummary: {kritik} Critical, {guncelleme} Outdated, {len(results) - kritik - guncelleme} Up to date\n"
    )