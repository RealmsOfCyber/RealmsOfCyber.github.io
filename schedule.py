schedule_build = [
    {
        "time": "8:00 - 9:00",
        "title": "Registration"
    },
    {
        "time": "9:00 - 9:15",
        "title": "Acknowledgement of Country and Opening Words"
    },
    {
        "time": "9:15 - 9:35",
        "title": "This is a preso",
        "realm": "Space",
        "speaker": {
            "name": "Kylie McDevitt",
            "image": "kylie_mcdevitt.jpg"
        },
        "desc": "This is a sample preso."
    },
    {
        "time": "9:15 - 9:35",
        "title": "This is a preso",
        "realm": "Space",
        "speaker": {
            "name": "Kylie McDevitt",
            "image": "kylie_mcdevitt.jpg"
        },
        "desc": "This is a sample preso."
    },
    {
        "time": "4:55 - 5:00",
        "title": "Closing Words"
    },
    {
        "time": "5:00 - 6:30",
        "title": "Networking Session and Closing Reception"
    }
]

schedule = []
for schedule_item in schedule_build:
    if "speaker" not in schedule_item.keys():
        schedule += [schedule_item]
        continue
    match schedule_item["realm"]:
        case "Space":
            schedule_item["logo"] = "fa-satellite"
        case "Cognitive":
            schedule_item["logo"] = "fa-brain"
        case "Land":
            schedule_item["logo"] = "fa-truck"
        case "Sea":
            schedule_item["logo"] = "fa-ship"
        case "Air":
            schedule_item["logo"] = "fa-plane-departure"
        case "Biological":
            schedule_item["logo"] = "fa-dna"
        case "Multi":
            schedule_item["logo"] = "fa-earth-americas"
        case _:
            schedule_item["logo"] = "fa-earth-americas"
    schedule += [schedule_item]
