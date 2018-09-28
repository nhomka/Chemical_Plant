# Useful conversions

from math import *

# Mass Conversions


def lb_to_kg(lbs):
    kgs = lbs*.453592
    return kgs


def kg_to_lb(kgs):
    lbs = kgs/.453592
    return lbs


def g_to_kg(g):
    kg = g/1000
    return kg


def kg_to_g(kg):
    g = kg*1000
    return g


def g_to_lb(g):
    lb = g/453.592
    return lb


def lb_to_g(lb):
    g = lb*453.592
    return g


# Time Conversions
def years_to_weeks(years):
    weeks = floor(years*7)/365
    return weeks


def years_to_days(years):
    days = years*365
    return days


def years_to_hours(years):
    hours = years*(365*24)
    return hours


def years_to_minutes(years):
    minutes = years*(365*24*60)
    return minutes


def weeks_to_years(weeks):
    years = (weeks*7)/365
    return years


def weeks_to_days(weeks):
    days = weeks*7
    return days


def weeks_to_hours(weeks):
    hours = weeks*7*24
    return hours


def weeks_to_minutes(weeks):
    minutes = weeks*7*24*60
    return minutes


def days_to_years(days):
    years = days/365
    return years


def days_to_weeks(days):
    weeks = days/7
    return weeks


def days_to_hours(days):
    hours = days*24
    return hours


def days_to_minutes(days):
    minutes = days*60*24
    return minutes


def hours_to_years(hours):
    years = hours/(24*365)
    return years


def hours_to_weeks(hours):
    weeks = hours/(24*7)
    return weeks


def hours_to_days(hours):
    days = hours/24
    return days


def hours_to_minutes(hours):
    minutes = hours*60
    return minutes


def minutes_to_years(minutes):
    years = minutes/(60*24*365)
    return years


def minutes_to_weeks(minutes):
    weeks = minutes/(24*60*7)
    return weeks


def minutes_to_days(minutes):
    days = minutes/(24*60)
    return days


def minutes_to_hours(minutes):
    hours = minutes/60
    return hours
