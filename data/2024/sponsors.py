# Sponsors data format:
# sponsors = {
#     "Platinum": [
#         {
#             "name": "Sponsor Name",
#             "url": "https://sponsor-website.com",
#             "logo": "sponsor_logo.png",
#             # Optional: custom dimensions (if not provided, defaults are used based on tier)
#             "height": 110,  # Optional
#             "width": 320   # Optional
#         },
#         ...
#     ],
#     "Gold": [...],
#     "Silver": [...],
#     "Bronze": [...]
# }
# Default dimensions by tier (if not specified):
# - Platinum: 110x320
# - Gold: 90x260
# - Silver: 70x220
# - Bronze: 60x180
# Images should be placed in: site/assets/images/{year}/sponsors/
sponsors = {
    "Platinum": [],
    "Gold": [],
    "Silver": [],
    "Bronze": [],
}
