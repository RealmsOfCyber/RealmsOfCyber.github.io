schedule_build = [
    {
        "time": "8:00 - 8:45",
        "title": "Registration"
    },
    {
        "time": "8:45 - 9:00",
        "title": "Theater Open"
    },
    {
        "time": "9:00 - 9:15",
        "title": "Acknowledgement of Country and Opening Words"
    },
    {
        "time": "9:15 - 9:35",
        "title": "Keynote goes here",
        "realm": "Space",
        "speaker": {
            "name": "TBD",
            "image": "default.png"
        },
        "desc": "This is a sample preso."
    },
    {
        "time": "9:35 - 9:50",
        "title": "This is a preso",
        "realm": "Multi",
        "speaker": {
            "name": "Kylie McDevitt",
            "image": "kylie_mcdevitt.jpg"
        },
        "desc": "This is a sample preso."
    },
    {
        "time": "9:50 - 10:05",
        "title": "This is a preso",
        "realm": "Air",
        "speaker": {
            "name": "Mike Monik",
            "image": "mike_monnik.jpeg"
        },
        "desc": "This is a sample preso."
    },
    {
        "time": "10:05 - 10:20",
        "title": "This is a preso",
        "realm": "Sea",
        "speaker": {
            "name": "Bradley Butler",
            "image": "bradley_butler.jpg"
        },
        "desc": "This is a sample preso."
    },
    {
        "time": "10:20 – 10:35",
        "title": "TBD",
        "realm": "Multi",
        "speaker": {
            "name": "TBD",
            "image": "default.png"
        },
        "desc": "TBD"
    },
    {
        "time": "10:35 – 10:45",
        "title": "Group Q&A Session"
    },
    {
        "time": "10:45 – 11:30",
        "title": "Morning Tea Break"
    },
    {
        "time": "11:30 – 11:45",
        "title": "TBD",
        "realm": "Multi",
        "speaker": {
            "name": "TBD",
            "image": "default.png"
        },
        "desc": "TBD"
    },
    {
        "time": "11:45 – 12:00",
        "title": "TBD",
        "realm": "Multi",
        "speaker": {
            "name": "TBD",
            "image": "default.png"
        },
        "desc": "TBD"
    },
    {
        "time": "12:00 – 12:15",
        "title": "Joint Preso",
        "realm": "Multi",
        "speaker": {
            "name": "TBD",
            "image": "default.png"
        },
        "desc": "TBD"
    },
    {
        "time": "12:15 – 12:25",
        "title": "Group Q&A Session"
    },
    {
        "time": "12:25 – 12:30",
        "title": "Demo Announcement"
    },
    {
        "time": "12:30 – 13:40",
        "title": "Lunch Break"
    },
    {
        "time": "13:40 – 13:55",
        "title": "TBD",
        "realm": "Multi",
        "speaker": {
            "name": "TBD",
            "image": "default.png"
        },
        "desc": "TBD"
    },
    {
        "time": "13:55 – 14:10",
        "title": "TBD",
        "realm": "Multi",
        "speaker": {
            "name": "TBD",
            "image": "default.png"
        },
        "desc": "TBD"
    },
    {
        "time": "14:10 – 14:25",
        "title": "TBD",
        "realm": "Multi",
        "speaker": {
            "name": "TBD",
            "image": "default.png"
        },
        "desc": "TBD"
    },
    {
        "time": "14:25 – 14:40",
        "title": "TBD",
        "realm": "Multi",
        "speaker": {
            "name": "TBD",
            "image": "default.png"
        },
        "desc": "TBD"
    },
    {
        "time": "14:40 – 14:50",
        "title": "Group Q&A Session"
    },
    {
        "time": "14:50 – 15:45",
        "title": "Afternoon Tea Break"
    },
    {
        "time": "15:45 – 16:00",
        "title": "TBD",
        "realm": "Multi",
        "speaker": {
            "name": "TBD",
            "image": "default.png"
        },
        "desc": "TBD"
    },
    {
        "time": "16:00 – 16:15",
        "title": "TBD",
        "realm": "Multi",
        "speaker": {
            "name": "TBD",
            "image": "default.png"
        },
        "desc": "TBD"
    },
    {
        "time": "16:15 – 16:30",
        "title": "TBD",
        "realm": "Multi",
        "speaker": {
            "name": "TBD",
            "image": "default.png"
        },
        "desc": "TBD"
    },
    {
        "time": "16:30 – 16:45",
        "title": "TBD",
        "realm": "Multi",
        "speaker": {
            "name": "TBD",
            "image": "default.png"
        },
        "desc": "TBD"
    },
    {
        "time": "16:45 – 16:55",
        "title": "Group Q&A Session"
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
