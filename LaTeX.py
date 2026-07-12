from pylatex import (
    Document,
    Section,
    Subsection,
    Figure,
    Tabular,
    NoEscape,
    Command
)
from pylatex.utils import bold
import os
import subprocess
from collections.abc import Mapping, Sequence
from typing import Any


def create_latex_report(
    results: Mapping[str, Any],
    Orte: Sequence[str],
    filename: str = "Auswertung",
    title: str = "Auswertung der Fahrraddaten"
) -> None:
    """
    Erstellt einen LaTeX-Bericht mit den berechneten Kenngrößen und
    allen erzeugten Diagrammen.

    Die Funktion erzeugt ein LaTeX-Dokument mit einer Titelseite,
    einer Tabelle der wichtigsten Auswertungsergebnisse sowie einer
    Abbildung für jede im aktuellen Arbeitsverzeichnis vorhandene
    PNG-Datei.
    """

    doc = Document(documentclass="article")

    # Pakete
    doc.packages.append(Command("usepackage", "float"))
    doc.packages.append(Command("usepackage", "graphicx"))
    doc.packages.append(Command("usepackage", "booktabs"))
    doc.packages.append(Command("usepackage", "geometry"))
    doc.packages.append(Command("geometry", "margin=2.5cm"))

    # Titelseite
    doc.preamble.append(Command("title", title))
    doc.preamble.append(Command("author", ""))
    doc.preamble.append(Command("date", NoEscape(r"\today")))

    doc.append(NoEscape(r"\maketitle"))

    with doc.create(Section("Berechnete Kennwerte")):
        with doc.create(Tabular("lr")) as table:
            table.add_hline()
            table.add_row((bold("Kennwert"), bold("Wert")))
            table.add_hline()
            table.add_row(("Gesamtstrecke",
                           f"{results['Gesamtstrecke_Original']:.1f} m"))
            table.add_row(("Durchschnittsgeschwindigkeit",
                           f"{results['Durchschnittsgeschwindigkeit']:.2f} m/s"))
            table.add_row(("Maximalleistung",
                           f"{results['P_max']:.1f} W"))
            table.add_row(("Gesamtzeit",
                           str(results["Gesamtzeit"])))
            table.add_row(("Gesamter Anstieg",
                           f"{results['Anstieg']:.1f} m"))
            table.add_row(("Gesamter Abstieg",
                           f"{results['Abstieg']:.1f} m"))

            table.add_hline()
    
    orte_text = ", ".join(Orte)
    with doc.create(Section("Durchfahrene Orte")):
        doc.append(orte_text)

    with doc.create(Section("Diagramme")):
        png_files = sorted(
            f for f in os.listdir(".")
            if f.endswith(".png")
        )
        for image in png_files:
            plotname = os.path.splitext(image)[0]
            with doc.create(Subsection(plotname)):
                with doc.create(Figure(position="H")) as fig:
                    fig.add_image(image, width=NoEscape(r"0.95\textwidth"))
                    fig.add_caption(plotname)

    doc.generate_tex(filepath="Auswertung")
    #doc.generate_pdf(filename, clean_tex=False, clean=True)
    print(f"Bericht '{filename}.tex' wurde erstellt.")
  
