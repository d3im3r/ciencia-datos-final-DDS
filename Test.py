import gpxpy
import pandas as pd

def read_gpx(file: str) -> pd.DataFrame:
    df = None
    points = []
    with open(file) as f:
        gpx = gpxpy.parse(f)
    for segment in gpx.tracks[0].segments:
        for p in segment.points:
            points.append({
                'time': p.time,
                'latitude': p.latitude,
                'Longitude': p. longitude,
                'elevation': p.elevation
            })
    df = pd.DataFrame.from_records(points)
    return df

df1 = read_gpx('recovery.01-Mar-2022-1533.gpx')