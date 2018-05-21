from functools import singledispatch
from business.offence import Offence
from business.location import Location
from business.crime_report import CrimeReport
from flask import url_for


@singledispatch
def to_serializable(val):
    return str(val)


@to_serializable.register(Offence)
def ts_offence(val: Offence):
    return {
        "id": str(val.id),
        "links": {
            "self": url_for("offences_resource.getOffence", id=str(val.id), _external=True),
            "crime_reports": url_for("offences_resource.getCrimesForOffence", id=str(val.id), _external=True)
        },
        "category": val.category,
        "subcategory": val.subcategory
    }


@to_serializable.register(Location)
def ts_location(val: Location):
    return {
        "id": str(val.id),
        "links": {
            "self": url_for("locations_resource.getLocation", id=str(val.id), _external=True),
            "crime_reports": url_for("locations_resource.getCrimesForLocation", id=str(val.id), _external=True)
        },
        "stats_area": val._statsArea,
        "lga": val.lga
    }


@to_serializable.register(CrimeReport)
def ts_crime_report(val: CrimeReport):
    return {
        "id": str(val.id),
        "links": {
            "self": url_for("crimes_resource.getCrime", id=str(val.id), _external=True)
        },
        "crime_count": val.crime_count,
        "time_period": val.time_period,
        "location": {
            "id": str(val.location.id),
            "summary": val.location.lga,
            "url": url_for("locations_resource.getLocation", id=str(val.location.id), _external=True)
        },
        "offence": {
            "id": str(val.offence.id),
            "summary": val.offence.category,
            "url": url_for("offences_resource.getOffence", id=str(val.offence.id), _external=True)
        }
    }
