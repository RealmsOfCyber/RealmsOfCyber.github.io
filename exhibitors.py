exhibitors = [
    {
        "name": "Ocebile",
        "url": "https://www.ocebile.com/",
        "logo": "ocebile.png"
    },
    {
        "name": "McBathy",
        "url": "https://mcbathy.com/",
        "logo": "mcbathy.png"
    }, 
    {
        "name": "Roo-ver",
        "url": "https://www.space.gov.au/meet-roo-ver",
        "logo": "roo-ver.jpg"
    }
]

for exhibitor in exhibitors:
    # Matching "Platinum" sponsor height and width
    exhibitor["height"] = 110
    exhibitor["width"] = 320
