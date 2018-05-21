from csv import DictReader
from rx import Observable
import persistence.mongo_repository as repo
from .crime_report import CrimeReport
from .location import Location
from .offence import Offence


def process_csv(filename: str) -> None:
    csvObservable = Observable.from_(DictReader(  # pylint: disable=no-member
        open(filename, "r")))
    csvObservable.subscribe(_persist_crime_reports)


def _persist_crime_reports(csv_line) -> None:
    offence: Offence = _get_offence(csv_line)
    location: Location = _get_location(csv_line)

    for date_field in list(csv_line.keys())[4:]:
        crime_report: CrimeReport = CrimeReport(
            time_period=date_field, crime_count=csv_line[date_field], location=location, offence=offence)
        repo.persist_crime_report(crime_report)


def _get_location(csv_line) -> Location:
    return Location(statsArea=str(csv_line["Statistical Division or Subdivision"]), lga=str(csv_line["LGA"]))


def _get_offence(csv_line) -> Offence:
    return Offence(category=str(csv_line["Offence category"]), subcategory=str(csv_line["Subcategory"]))
